from django.contrib import admin

from abouts.models import Experience, Skill, SkillCategory, ExperienceCategory

admin.site.register(Experience)
admin.site.register(ExperienceCategory)
admin.site.register(Skill)
admin.site.register(SkillCategory)
