from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ValidationError

from ..models import Post


def search_result(request):
    """ /search/?q=query """
    search_text = request.GET.get('q', '')
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')

    posts = None
    errors = []

    if search_text:
        posts = Post.objects.filter(
            Q(published=True)
            & (Q(title__icontains=search_text)
               | Q(content__icontains=search_text)
               )
        )

    if from_date:
        # assume if a time wasn't specified they want throughout the entire day
        from_date += "T23:59" if "T" not in from_date else ''
        try:
            posts = posts.filter(updated_at__gt=from_date)
        except ValidationError:
            errors.append("Invalid from date: " + from_date)

    if to_date:
        # assume if a time wasn't specified they want throughout the entire day
        to_date += "T23:59" if "T" not in to_date else ''
        try:
            posts = posts.filter(updated_at__lt=to_date)
        except ValidationError:
            errors.append("Invalid to date: " + to_date)

    print(errors)
    return render(request, 'blog/search_result.html', {
        'search_text': search_text,
        'posts': posts,
        'errors': errors
    })
