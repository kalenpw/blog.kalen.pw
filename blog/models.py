from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
import re


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    published = models.BooleanField(null=False, default=False)
    image = models.ImageField(upload_to='blog/',
                              null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, blank=True)

    """Replaces mark down code blocks with <language> for brevity"""
    def preview_text(self):
        pattern = re.compile("```([A-Za-z]+)[^`]+```")
        match = pattern.search(self.content)
        # if we matched show code type in brackets
        if match:
            return re.sub(pattern, "<" + match.group(1) + ">", self.content)
        # no match just show generic code
        else:
            return re.sub("```[^`]+```", "<code>", self.content)

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
