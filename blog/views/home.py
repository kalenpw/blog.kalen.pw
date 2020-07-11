from django.shortcuts import render

from ..models import Post

def home(request):
    latest_posts = Post.objects.filter(published=True).order_by('-updated_at')[:7]
    return render(request, 'blog/home.html', {'posts': latest_posts})
