from django.urls import path, re_path
from assignments import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'assignments'

urlpatterns = [
    path('create/', views.CreateAssignment.as_view(), name="create"),  # 使用 path
    re_path(r'^detail/(?P<pk>[-\w]+)/$', views.AssignmentDetail.as_view(), name='detail'),  # 使用 re_path
    re_path(r'^update/(?P<pk>[-\w]+)/$', views.UpdateAssignment.as_view(), name='update'),  # 使用 re_path
    re_path(r'^delete/(?P<pk>[-\w]+)/$', views.DeleteAssignment.as_view(), name="delete"),  # 使用 re_path
    path('submit/', views.SubmitAssignmentView.as_view(), name="submit"),  # 使用 path
    re_path(r'^submission/detail/(?P<pk>[-\w]+)/$', views.SubmitAssignmentDetail.as_view(), name="submit_detail"),  # 使用 re_path
    re_path(r'^submission/delete/(?P<pk>[-\w]+)/$', views.delete_view, name="submit_delete"),  # 使用 re_path
    re_path(r'^grade/(?P<pk>[-\w]+)/$', views.grade_assignment, name='grade'),  # 使用 re_path
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
