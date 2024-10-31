from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course
from django.shortcuts import render

class UserProfile(LoginRequiredMixin, generic.ListView): #这个混合类用于确保用户在访问该视图之前已经登录。如果用户未登录，Django 会自动重定向他们到登录页面
    model = Course
    template_name = 'user_profile.html'

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html') 