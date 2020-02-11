from django.db import models
import datetime
import pytz

"""A message board"""


class BoardManager(models.Manager):
    def slug_matches(self, slug):
        boards = Board.objects.all()
        matchedBoard = None
        for board in boards:
            if slug == board.slug():
                matchedBoard = board
        return matchedBoard


class Board(models.Model):
    objects = BoardManager()
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def post_count(self):
        return len(self.get_all_posts())

    def latest_post_time(self):
        base_date = datetime.datetime(1900, 1, 1, tzinfo=pytz.UTC)
        latest_post = base_date
        for post in self.get_all_posts():
            if post.created_at and post.created_at > latest_post:
                latest_post = post.created_at
            # prefer updated time
            if post.updated_at and post.updated_at > latest_post:
                latest_post = post.updated_at
        if base_date == latest_post:
            return None
        return latest_post

    def get_all_posts(self):
        posts = []
        for topic in self.topics.all():
            for post in topic.posts.all():
                posts.append(post)
        return posts

    def slug(self):
        return self.name.lower()
