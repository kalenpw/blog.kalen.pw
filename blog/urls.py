from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.home, name='home'),
    path('tag/<slug:tag_name>', views.list_result, name='list_result'),
    path('posts/<int:post_id>/<slug:post_name>', views.post_detail, name='post_detail')
]
