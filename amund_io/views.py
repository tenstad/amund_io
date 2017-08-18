from django.views.generic import TemplateView
from articles.models import Article

class Index(TemplateView):
    template_name = 'amund_io/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'articles': Article.objects.all()
        })
        return context
