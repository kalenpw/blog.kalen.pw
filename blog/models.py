from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    published = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.title + ": " + self.content[:10]


class Comment(models.Model):
    text = models.TextField(max_length=2000)
    user_id = models.ForeignKey(
        User, related_name='blog_comments', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]


class Tag(models.Model):
    name = models.CharField(max_length=40)
    post = models.ForeignKey(
        Post, null=False, related_name='tags', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    