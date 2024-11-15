from django.db import models
from courses.models import Course
# Create your models here.
from django.utils import timezone


class Quiz(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')

    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    @property
    def is_show(self):
        if self.questions.count() == 0:
            return False
        return True

    @property
    def is_start(self):
        current_time = timezone.now()
        if current_time < self.start_time or current_time > self.end_time:
            return False
        return True


class Questions(models.Model):
    no = models.CharField(max_length=64)
    description = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        unique_together = ('quiz_id', 'no')


class Choices(models.Model):
    text = models.CharField(max_length=256)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text


class Transcripts(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, blank=True, null=True, related_name='transcripts')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='transcripts')
    score = models.IntegerField(default=60)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() + " " + str(self.score)


class Record(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choices, on_delete=models.CASCADE)
    transcripts = models.ForeignKey(Transcripts, on_delete=models.CASCADE, related_name='records')

    @property
    def is_correct(self):
        return self.answer.is_correct
