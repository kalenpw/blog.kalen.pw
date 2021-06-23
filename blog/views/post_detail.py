from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponseNotFound

from ..models import Post
from ..forms import CommentForm


def post_detail(request, post_id, post_name):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()

    show_unpublished = request.user.is_superuser and request.GET.get('preview') == 'true'

    if post.slug() != post_name or not post.published:
        if not show_unpublished:
            raise Http404("Post not found")

    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})
