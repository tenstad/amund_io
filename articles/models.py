from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = MarkdownxField()
    creation_date = models.DateTimeField(default=timezone.now)
