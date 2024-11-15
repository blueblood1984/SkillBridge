from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course, Enrollment
from assignments.models import Assignment
from quizzes.models import Quiz
from resources.models import Resource
from lectures.models import Lecture


# Create your views here.
class CreateCourse(LoginRequiredMixin, generic.CreateView):
    fields = ('course_name', 'course_description')
    model = Course

    def get(self, request, *args, **kwargs):
        self.object = None
        context_dict = self.get_context_data()
        context_dict.update(user_type=self.request.user.user_type)
        return self.render_to_response(context_dict)

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(CreateCourse, self).form_valid(form)


class CourseDetail(generic.DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        assignments = Assignment.objects.filter(course=self.kwargs['pk'])
        resources = Resource.objects.filter(course=self.kwargs['pk'])
        lectures = Lecture.objects.filter(course=self.kwargs['pk'])
        quizzes = Quiz.objects.filter(course=self.kwargs['pk'])
        context = super(CourseDetail, self).get_context_data(**kwargs)
        context['assignments'] = assignments
        context['resources'] = resources
        context['lectures'] = lectures
        context['quizzes'] = quizzes
        return context


class ListCourse(generic.ListView):
    model = Course


class EnrollCourse(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('courses:detail', kwargs={'pk': self.kwargs.get('pk')})

    def get(self, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs.get('pk'))

        try:
            Enrollment.objects.create(student=self.request.user, course=course)
        except:
            messages.warning(self.request, 'You are already enrolled in the course.')
        else:
            messages.success(self.request, 'You are now enrolled in the course.')
        return super().get(self.request, *args, **kwargs)


class UnenrollCourse(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('courses:detail', kwargs={'pk': self.kwargs.get('pk')})

    def get(self, *args, **kwargs):

        try:
            enrollment = Enrollment.objects.filter(
                student=self.request.user,
                course__pk=self.kwargs.get('pk')
            ).get()
        except Enrollment.DoesNotExist:
            messages.warning(self.request, 'You are not enrolled in this course.')
        else:
            enrollment.delete()
            messages.success(self.request, 'You have unenrolled from the course.')
        return super().get(self.request, *args, **kwargs)


@login_required
def member_list(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    members = Enrollment.objects.filter(course=course)
    return render(request, 'courses/member_list.html', locals())


@login_required
def delete_course(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("courses:list")
    return render(request, 'courses/course_confirm_delete.html', locals())
