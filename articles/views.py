from django.views.generic import TemplateView

from articles.models import Article


class ArticleView(TemplateView):
    template_name = 'articles/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context.update({
                'article': Article.objects.get(id=kwargs['image_id'])
            })
        except Article.DoesNotExist:
            pass
        return context
