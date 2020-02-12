from ..models import Board
from django.shortcuts import render

def home(request):
    boards = Board.objects.all()
    return render(request, 'forum/home.html', {'boards': boards})