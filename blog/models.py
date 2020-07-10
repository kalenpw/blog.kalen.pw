import re

from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


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
    previous = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='next_reverse' ,null=True)
    next = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='previous_reverse', null=True)

    """Replaces mark down code blocks with <language> for brevity"""

    def preview_text(self):
        post_text = self.content
        post_text = post_text.replace('#', '')
        pattern = re.compile("<div class=\"code-block dark\">[\s\S]*?<\/div>")
        pattern = re.compile("```([A-Za-z]+)[^`]+```")
        match = pattern.search(post_text)
        # if we matched show code type in brackets
        if match:
            return re.sub(pattern, "<" + match.group(1) + ">", post_text)
        # no match just show generic code
        else:
            return re.sub("```[^`]+```", "<code>", post_text)

    def slug(self):
        return self.title.lower().replace(" ", "-").replace("&", "and")

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
