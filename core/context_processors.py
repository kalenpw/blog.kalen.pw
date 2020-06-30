from collections import defaultdict

from blog.models import Post


def get_month_by_number(month_num):
    months = [
        'Jan.',
        'Feb.',
        'Mar.',
        'Apr.',
        'May.',
        'Jun.',
        'Jul.',
        'Aug.',
        'Sep.',
        'Oct.',
        'Nov.',
        'Dec.'
    ]
    return months[month_num - 1]


def get_post_meta_info(request):
    """ Returns a dict with how many posts are published in each year/month"""
    post_meta_info = defaultdict(int)

    posts = Post.objects.all().order_by('-updated_at')

    for post in posts:
        year = post.updated_at.year
        month = post.updated_at.month

        if post_meta_info[year] == 0:
            post_meta_info[year] = defaultdict(int)

        post_meta_info[year]['count'] += 1
        post_meta_info[year][get_month_by_number(month)] += 1

    return {'post_meta_info': post_meta_info}
