from django.views.generic import TemplateView
from articles.models import Article
from abouts.models import Experience, Skill

class Index(TemplateView):
    template_name = 'amund_io/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'articles': Article.objects.all()
        })
        return context


def group_by_category(model, fields):
    item_dict = {}
    items = model.objects.values('category__title', *fields).order_by('category__title')
    for item in items:
        if item['category__title'] in item_dict:
            item_dict[item['category__title']].append(item)
        else:
            item_dict[item['category__title']] = [item]
    return item_dict

class About(TemplateView):
    template_name = 'amund_io/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'skills': group_by_category(Skill, ('skill',)),
            'experiences': group_by_category(Experience, ('title', 'description', 'start_year', 'end_year')),
        })

        print(context)

        return context
