from django.shortcuts import render

from ..models import Post, Tag

def list_result(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render(request, 'blog/list_result.html', {'posts': posts, 'tag_name': tag_name})