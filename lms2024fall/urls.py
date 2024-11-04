from django.contrib import admin
from django.urls import path, include  # use path and re_path
from assignments import views
from lms2024fall import views as project_views
from django.urls import re_path  # Import re_path for regex URL patterns

urlpatterns = [
    path('', project_views.index, name="home"),  # Replaced url() with path()
    path('contact', project_views.contact, name="contact"), 
    path('about', project_views.about, name="about"),   
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),  
    path('courses/', include('courses.urls', namespace="courses")), 
    path('assignments/', include('assignments.urls', namespace='assignments')), 
    path('resources/', include('resources.urls', namespace="resources")), 
    re_path(r'^user_profile/(?P<pk>[-\w]+)/$',project_views.UserProfile.as_view(), name="profile"),
]
