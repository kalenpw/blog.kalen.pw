import datetime

from django.core.management.base import BaseCommand
from blog.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.date.today()
        for i in range(10):
            post = Post(
                title=f"Test post {i}",
                published=True,
                updated_at=today + datetime.timedelta(days=i),
                created_at=today + datetime.timedelta(days=i),
            )
            post.save()
