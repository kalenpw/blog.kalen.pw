from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Post


def home(request, page_num=1):
    posts = Paginator(Post.objects.filter(published=True).order_by('-updated_at'), 4)
    return render(request, 'blog/home.html', {'posts': posts.get_page(page_num)})
