from django.shortcuts import render

from blog.models import Post

def generate_rss(request):
    posts = Post.objects.all()
    return render(request, 'rss/rss.html', {'posts': posts} ,content_type="application/xhtml+xml")