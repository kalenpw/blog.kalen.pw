from django.shortcuts import render


def by_date(request, year, month=''):
    """ GET /date/$year/$month """
    return render(request, 'blog/home.html')
