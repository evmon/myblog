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

    def get_absolute_url(self):
        return reverse('blog_part:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

