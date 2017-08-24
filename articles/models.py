from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from files.models import Image
from tags.models import Tag
from markdown import markdown

class Article(models.Model):
    title = models.CharField(max_length=50)
    ingress = models.TextField(max_length=500, blank=True)
    content = models.TextField(max_length=4000, blank=True)
    thumbnail = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(app_label)s_%(class)s_related_thumb')
    tags = models.ManyToManyField(Tag, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
