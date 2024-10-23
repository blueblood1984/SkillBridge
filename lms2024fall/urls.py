from django.contrib import admin
from django.urls import path, include  # use path and re_path
from assignments import views
from lms2024fall import views as project_views
from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
from django.urls import re_path  # Import re_path for regex URL patterns

urlpatterns = [
    path('', project_views.index, name="home"),  # Replaced url() with path()
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),  # Replaced url() with path()
    path('courses/', include('courses.urls', namespace="courses")),  # Replaced url() with path()
    path('assignments/', include('assignments.urls', namespace='assignments')),  # Replaced url() with path()
    path('resources/', include('resources.urls', namespace="resources")),  # Replaced url() with path()
    re_path(r'^user_profile/(?P<pk>[-\w]+)/$',  # Used re_path() for regex patterns
        project_views.UserProfile.as_view(), name="profile"),
    path('graphql/', FileUploadGraphQLView.as_view(graphiql=True)),
]
