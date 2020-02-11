from django.urls import path

from . import views

urlpatterns = [
    path('<slug:board_name>/<int:board_id>/',
         views.board_topics, name='board_topics'),
    # new topic on board
    path('<slug:board_name>/<int:board_id>/new/',
         views.new_topic, name='new_topic'),
    # view topic on board
    path('<slug:board_name>/topics/<int:topic_id>/',
         views.topic, name='topic'),
    # new post for topic on board
    path('<slug:board_name>/topics/<int:topic_id>/new/post/',
         views.NewPostView.as_view(), name='new_post'),
]
