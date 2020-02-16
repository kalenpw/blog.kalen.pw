from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Board, Topic, Post
from ..forms import NewTopicForm
from django.contrib.auth.decorators import login_required
from pprint import pprint


@login_required
def new_topic(request, board_name, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('forum/board_topics', board_name=board.slug(), board_id=board.id)
    else:
        form = NewTopicForm()
    return render(request, 'forum/new_topic.html', {'board': board, 'form': form})
