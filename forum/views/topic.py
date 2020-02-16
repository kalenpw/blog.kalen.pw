from django.shortcuts import get_object_or_404, render
from ..models import Topic

def topic(request, board_name, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'forum/topic.html', {'board': topic.board, 'topic': topic})