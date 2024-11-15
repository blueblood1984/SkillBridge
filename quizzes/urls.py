from django.urls import path
from quizzes import views
app_name = "quizzes"

urlpatterns = [
    path('create/', views.create_quiz, name='create'),
    path('detail/<int:pk>/', views.quiz_detail, name='detail'),
    path('update/<int:pk>/', views.update_quiz, name='update'),
    path('delete/<int:pk>/', views.delete_quiz, name='delete'),
    path('add_questions/<int:quiz_id>/', views.add_questions, name='add_questions'),
    path('delete_questions/<int:pk>/', views.delete_questions, name='delete_questions'),
    path('start_quiz/<int:pk>/', views.start_quiz, name='start_quiz'),
    path('transcript/list/<int:quiz_id>/', views.transcript_list, name='transcript_list'),
    path('transcript/rw/<int:quiz_id>/', views.rw_distribution_chart, name='rw_distribution_chart'),
    path('transcript/grade/<int:quiz_id>/', views.grade_distribution_chart, name='grade_distribution_chart'),
    path('transcript/detail/<int:pk>/', views.transcript_detail, name='transcript_detail'),
    path('transcript/profile/<int:quiz_id>/', views.my_transcript, name='my_transcript'),
]