from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    published = models.BooleanField(null=False, default=False)
    image = models.ImageField(upload_to='blog/',
                              null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, blank=True)

    def slug(self):
        return self.title.lower().replace(" ", "-")

    def __str__(self):
        return self.title + ": " + self.content[:10]


class Comment(models.Model):
    text = models.CharField(max_length=2000)
    user = models.ForeignKey(
        User, related_name='blog_comments', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.text[:20]
