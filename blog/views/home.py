from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from ..models import Post

POSTS_ON_HOMEPAGE = 4
POSTS_ON_PAGINATED = 6


def home(request):
    posts = Paginator(Post.objects.filter(published=True).order_by('-updated_at'), 4)
    return render(request, 'blog/home.html', {'posts': posts.get_page(1), 'home_page': True})


def home_paginated(request, page_num):
    posts = Paginator(Post.objects.filter(published=True).order_by('-updated_at'), 4)
    # keep our URL clean so instead of /page/1/ we just have /
    if page_num == 1:
        return redirect('blog:home')
    context = {
        'posts': posts.get_page(page_num),
        'home_page': False,
    }

    return render(request, 'blog/home_paginated.html', context)
