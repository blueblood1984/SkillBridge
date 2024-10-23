from django.urls import path, re_path
from resources import views

app_name = "resources"

urlpatterns = [
    path('create/', views.CreateResource.as_view(), name="create"),  # 使用 path
    re_path(r'^delete/(?P<pk>[-\w]+)/$', views.delete_view, name='delete'),  # 使用 re_path 处理带有正则表达式的路径
]
