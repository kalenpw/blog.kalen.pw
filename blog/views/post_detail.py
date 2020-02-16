from django.shortcuts import render
from django.http import HttpResponseNotFound

from ..models import Post

def post_detail(request, post_id, post_name):
    post = Post.objects.get(id=post_id)
    if post.slug() != post_name:
        return HttpResponseNotFound("404: No post found")
    return render(request, 'blog/post_detail.html', {'post': post})