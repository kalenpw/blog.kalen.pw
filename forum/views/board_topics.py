from django.shortcuts import render, get_object_or_404
from ..models import Board


def board_topics(request, board_name, board_id):
    board = get_object_or_404(Board, id=board_id)
    return render(request, 'topics.html', {'board': board})
