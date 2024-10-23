from django.urls import path, re_path
from courses import views

app_name = "courses"

urlpatterns = [
    path('new/', views.CreateCourse.as_view(), name="create"),  # 简单路径使用 path
    re_path(r'^detail/(?P<pk>[-\w]+)/$', views.CourseDetail.as_view(), name='detail'),  # 正则表达式使用 re_path
    path('all/', views.ListCourse.as_view(), name="list"),  # 简单路径使用 path
    re_path(r'^enroll/(?P<pk>[-\w]+)/$', views.EnrollCourse.as_view(), name='enroll'),  # 正则表达式使用 re_path
    re_path(r'^unenroll/(?P<pk>[-\w]+)/$', views.UnenrollCourse.as_view(), name='unenroll'),  # 正则表达式使用 re_path
]
