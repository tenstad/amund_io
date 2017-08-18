from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from files.models import Image
from tags.models import Tag

class Article(models.Model):
    title = models.CharField(max_length=50)
    ingress = MarkdownxField(blank=True)
    content = MarkdownxField(blank=True)
    thumbnail = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True, related_name='%(app_label)s_%(class)s_related_thumb')
    tags = models.ManyToManyField(Tag, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
