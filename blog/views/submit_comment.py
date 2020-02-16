from django.shortcuts import redirect
from django.urls import reverse


def submit_comment(request, post_id, post_name):
    if request.POST:
        return redirect(reverse('blog:post_detail', args=(post_id, post_name)))
    else:
        return redirect(reverse('blog:home'))