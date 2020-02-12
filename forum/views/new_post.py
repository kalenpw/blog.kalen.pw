from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from ..forms import NewPostForm
from ..models import Board, Topic


class NewPostView(View):
    def render_form(self, request, board, topic, form):
        return render(request, 'new_post.html', {
            'board': board, 'topic': topic, 'form': form
        })

    def post(self, request, board_name, topic_id):
        topic = Topic.objects.get(id=topic_id)
        form = NewPostForm(request.POST)
        board = Board.objects.slug_matches(board_name)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic', board_name=board.slug(), topic_id=topic_id)
        else:
            return self.render_form(request, board, topic, form)

    def get(self, request, board_name, topic_id):
        topic = Topic.objects.get(id=topic_id)
        board = Board.objects.slug_matches(board_name)
        form = NewPostForm()
        return self.render_form(request, board, topic, form)
