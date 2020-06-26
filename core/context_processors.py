from collections import defaultdict

from blog.models import Post


def get_post_meta_info(request):
    """ Returns a dict with how many posts are published in each year/month"""
    post_meta_info = defaultdict(int)

    posts = Post.objects.all()

    for post in posts:
        year = post.updated_at.year
        month = post.updated_at.month

        if post_meta_info[year] == 0:
            post_meta_info[year] = defaultdict(int)

        post_meta_info[year][month] += 1

    return {'post_meta_info': post_meta_info}
