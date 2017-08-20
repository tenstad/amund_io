from django.conf.urls import url
from .views import ArticleView

urlpatterns = [
    url(r'^(?P<image_id>[0-9]+)/$', ArticleView.as_view(), name='article'),
]
