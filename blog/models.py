import re

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class Tag(models.Model):
    name = models.CharField(max_length=40, validators=[alphanumeric])

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
    previous = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='next_reverse',
        null=True,
        default=None,
        blank=True
    )
    next = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='previous_reverse',
        null=True,
        default=None,
        blank=True
    )

    def get_previous(self):
        """ Returns previous article if it is published """
        if self.previous and self.previous.published:
            return self.previous
        return None

    def get_next(self):
        """ Returns next article if it is published """
        if self.next and self.next.published:
            return self.next
        return None

    def preview_text(self):
        """Replaces mark down code blocks with <language> for brevity"""
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
        """ Slug for URLs"""
        return re.sub(r'[^A-Za-z0-9 ]+', '', self.title.lower()).replace(' ', '-')

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
