from django.test import TestCase
from ..models import Board, Topic, Post
import datetime
import pytz

class BoardTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Dummy Board',
            description=''
        )
        topic = Topic.objects.create(
            subject='Test subj',
            board=self.board,
            starter=None
        )
        post = Post.objects.create(
            message='foobar',
            topic=topic,
            updated_at=datetime.datetime(2020, 11, 1, 5, 0, tzinfo=pytz.UTC),
            created_by=None
        )
        post = Post.objects.create(
            message='foobar',
            topic=topic,
            updated_at=datetime.datetime(2010, 11, 1, 5, 0, tzinfo=pytz.UTC),
            created_by=None
        )
        post = Post.objects.create(
            message='foobar',
            topic=topic,
            updated_at=datetime.datetime(2020, 11, 1, 4, 0, tzinfo=pytz.UTC),
            created_by=None
        )

    def test_board_post_count(self):
        self.assertEqual(3, self.board.post_count())

    def test_earliest_post(self):
        earliest = datetime.datetime(2020, 11, 1, 5, 0, tzinfo=pytz.UTC)
        self.assertEqual(earliest, self.board.latest_post_time())
