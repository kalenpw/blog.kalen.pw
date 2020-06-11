from django.shortcuts import render
from django.db.models import Q

from ..models import Post


def search_result(request):
    """ /search/?q=query """
    search_text = request.GET.get('q')
    if search_text:
        posts = Post.objects.filter(
            Q(title__contains=search_text)
            | Q(content__contains=search_text)
            | Q()
        )
    else:
        posts = []
        search_text = ''
    return render(request, 'blog/search_result.html', {
        'search_text': search_text,
        'posts': posts
    })
