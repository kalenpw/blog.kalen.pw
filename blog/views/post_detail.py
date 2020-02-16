from django.shortcuts import render
from django.http import HttpResponseNotFound

from ..models import Post
from ..forms import CommentForm


def post_detail(request, post_id, post_name):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    if post.slug() != post_name:
        return HttpResponseNotFound("404: No post found")
    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})
