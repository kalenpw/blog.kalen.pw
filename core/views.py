from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def error_404(request, exception=None):
    context = {}
    return render(request, 'core/404.html', context)
