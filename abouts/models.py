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
    description = models.TextField(max_length=300)
    start_year = models.IntegerField(default=defaut_year)
    end_year = models.IntegerField(default=defaut_year)
    category = models.ForeignKey(ExperienceCategory)

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Skill(models.Model):
    skill = models.CharField(max_length=50)
    category = models.ForeignKey(SkillCategory)

    def __str__(self):
        return self.skill
