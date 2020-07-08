from django.shortcuts import redirect
from django.urls import reverse

from ..models import Comment, Post


def submit_comment(request, post_id, post_name):
    if request.POST:
        text = request.POST['text']
        post = Post.objects.get(id=post_id)
        comment = Comment(text=text, user=request.user, post=post)
        comment.save()

        return redirect(reverse('blog:post_detail', args=(post_id, post_name)))
    else:
        return redirect(reverse('blog:home'))