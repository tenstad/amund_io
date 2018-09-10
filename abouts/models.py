from django.db import models
from django.utils import timezone


def defaut_year():
    return timezone.now().year


class ExperienceCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True)
    start_year = models.DateField(default=timezone.now)
    end_year = models.DateField(default=timezone.now)
    current = models.BooleanField(default=False)
    category = models.ForeignKey(ExperienceCategory, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['start_year']

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Skill(models.Model):
    skill = models.CharField(max_length=50)
    category = models.ForeignKey(SkillCategory, on_delete=models.SET_NULL, null=True)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.skill
