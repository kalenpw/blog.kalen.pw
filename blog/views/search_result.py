from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator

from ..models import Post


def search_result(request):
    """ /search/?q=query """
    search_text = request.GET.get('q', '')
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    on_date = request.GET.get('on')
    page = request.GET.get('page', 1)

    posts = Post.objects.all()
    errors = []
    date_search_text = ""

    if search_text:
        posts = posts.filter(
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
            date_search_text += f"from: {from_date} "
        except ValidationError:
            errors.append("Invalid from date: " + from_date)

    if to_date:
        # assume if a time wasn't specified they want throughout the entire day
        to_date += "T23:59" if "T" not in to_date else ''
        try:
            posts = posts.filter(updated_at__lt=to_date)
            date_search_text += f"to: {to_date} "
        except ValidationError:
            errors.append("Invalid to date: " + to_date)

    if on_date:
        # we have a month as well
        if "-" in on_date:
            year, month = on_date.split("-")
            posts = posts.filter(updated_at__year=year, updated_at__month=month)
        else:
            posts = posts.filter(updated_at__year=on_date)
        date_search_text += f"date: {on_date}"

    posts = Paginator(posts, 4)

    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    if date_search_text:
        date_search_text = f'[{date_search_text}]'
    else:
        date_search_text = ""

    if search_text:
        search_text = f'"{search_text}"'
    else:
        search_text = "[ALL]"

    return render(request, 'blog/search_result.html', {
        'search_text': f"{search_text} {date_search_text}",
        'posts': posts.get_page(page),
        'errors': errors,
        'parameters': parameters
    })
