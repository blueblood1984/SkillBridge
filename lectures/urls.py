from django.urls import path
from lectures.views import CreateLecture, delete_view

app_name = "lectures"

urlpatterns = [
    path('create/', CreateLecture.as_view(), name='create'),
    path('delele/<int:pk>', delete_view, name='delete')
]
