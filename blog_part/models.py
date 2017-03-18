from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone


@python_2_unicode_compatible
class Post(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('blog_part:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Comment(models.Model):

    post = models.ForeignKey('blog_part.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse('blog_part:add-comment', kwargs={'pk': self.pk})

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return '{0}|{1}'.format(self.author, self.text, self.approved_comment )