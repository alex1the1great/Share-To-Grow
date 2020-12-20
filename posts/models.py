from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    link = models.URLField(null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
