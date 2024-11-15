from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F, Count,Case, When, Value, IntegerField
from django.db.models import F, Count
from django.db.models.functions import Floor

from .models import Quiz, Questions, Choices, Transcripts, Record
from .forms import QuizForm, QuestionForm, ChoicesFormSet
from users.models import User


@login_required
def create_quiz(request):
    form = QuizForm(user=request.user)
    if request.method == 'POST':
        form = QuizForm(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
    return render(request, 'quizzes/quiz_form.html', locals())


@login_required
def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    user = User.objects.get(pk=request.user.pk)
    show_transcript = False
    if user.user_type == 1:
        transcript = Transcripts.objects.filter(quiz=quiz, user=user).first()
        if transcript:
            show_transcript = True
    else:
        transcript = Transcripts.objects.filter(quiz=quiz).first()

    return render(request, 'quizzes/quiz_detail.html', locals())


@login_required
def update_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    form = QuizForm(instance=quiz,user=request.user)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('quizzes:detail', pk=quiz.id)
    return render(request, 'quizzes/quiz_edit.html', locals())


@login_required
def delete_quiz(request, pk):
    obj = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        course_id = obj.course_id
        obj.delete()
        return redirect("courses:detail", pk=course_id)
    return render(request, 'quizzes/quiz_confirm_delete.html', locals())


@login_required
def add_questions(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    form = QuestionForm()
    choice_formset = ChoicesFormSet()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        choice_formset = ChoicesFormSet(request.POST, instance=form.instance)
        if form.is_valid() and choice_formset.is_valid():
            question = form.save(commit=False)
            question.no = quiz.questions.count() + 1
            question.quiz = quiz
            question.save()
            choice_formset.save()

            for choice_form in choice_formset:
                if choice_form.cleaned_data:
                    choice = choice_form.save(commit=False)
                    choice.question = question
                    choice.save()
        return redirect('quizzes:detail', pk=quiz_id)
    return render(request, 'quizzes/add_questions.html', locals())


@login_required
def edit_questions(request, pk):
    question = get_object_or_404(Questions, pk=pk)
    choices = question.choices.all()
    form = QuestionForm(instance=question)
    choice_formset = ChoicesFormSet(initial=choices)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        choice_formset = ChoicesFormSet(request.POST, instance=form.instance)
        if form.is_valid() and choice_formset.is_valid():
            form.save()
            choice_formset.save()
            return redirect('quizzes:detail', pk=question.quiz_id)
    return render(request, 'quizzes/add_questions.html', locals())


@login_required
def delete_questions(request, pk):
    question = get_object_or_404(Questions, pk=pk)
    quiz = question.quiz

    question.delete()

    questions = Questions.objects.filter(quiz=quiz)
    for idx, question in enumerate(questions):
        question.no = idx + 1
        question.save()

    return redirect('quizzes:detail', pk=quiz.id)


@login_required
def start_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == 'POST':
        data = request.POST
        questions = quiz.questions.all()
        transcript = Transcripts.objects.create(quiz=quiz, user=request.user)
        correct_count = 0
        records = []
        for question in questions:
            # get question choice val
            user_pick = int(data.get(question.no))
            print("user_pick ==>", user_pick)
            choice = Choices.objects.get(pk=user_pick)
            if choice.is_correct:
                print('true')
                correct_count += 1
            records.append(Record(answer=choice, quiz=quiz, transcripts=transcript, question=question))
        print(correct_count, questions.count())
        transcript.score = correct_count * 100 // questions.count()
        transcript.save()
        Record.objects.bulk_create(records)
        return render(request, 'quizzes/quiz_result.html', locals())
    return render(request, 'quizzes/start_quiz.html', locals())


@login_required
def transcript_list(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    transcripts = Transcripts.objects.filter(quiz_id=quiz_id)
    return render(request, 'transcripts/transcript_list.html', locals())


@login_required
def rw_distribution_chart(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    transcripts = Transcripts.objects.filter(quiz_id=quiz_id)
    # statistic wrong
    wrong_map = {}
    correct_map = {}

    total = transcripts.count()
    for transcript in transcripts:
        records = transcript.records.all()
        for record in records:
            key = record.question.no
            if key not in wrong_map:
                wrong_map[key] = 0
            if key not in correct_map:
                correct_map[key] = 0
            if not record.is_correct:
                wrong_map[key] += 1
            else:
                correct_map[key] += 1
    wrong_x = list(wrong_map.keys())
    wrong_y = list(wrong_map.values())
    correct_y = list(correct_map.values())
    return render(request, 'transcripts/rw_distribution_chart.html', locals())


@login_required
def grade_distribution_chart(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    transcripts = Transcripts.objects.filter(quiz_id=quiz_id)
    
    score_x = []
    score_y = []
    
    results = (
        transcripts
            .annotate(
                score_range=Case(
                    When(score=100, then=Value(90)),  
                    default=Floor(F('score') / 10) * 10,
                    output_field=IntegerField()
                )
            )
            .values('score_range')
            .annotate(count=Count('id'))
            .order_by('score_range')
    )
    
    score_ranges = [(i, i + 10) for i in range(0, 90, 10)] + [(90, 100)]
    
    for range_start in score_ranges:
        range_label = f'{range_start[0]}~{range_start[1]}'
        count = next((result['count'] for result in results if result['score_range'] == range_start[0]), 0)
        score_x.append(range_label)
        score_y.append(count)
    
    return render(request, 'transcripts/grade_distribution_chart.html', locals())


@login_required
def transcript_detail(request, pk):
    transcript = get_object_or_404(Transcripts, pk=pk)
    return render(request, 'transcripts/transcript_detail.html', locals())


@login_required
def my_transcript(request, quiz_id):
    transcript = Transcripts.objects.filter(quiz_id=quiz_id, user=request.user).order_by('-id').first()
    return render(request, 'transcripts/transcript_detail.html', locals())
