from django.conf.urls import url
from .views import DemoView, predict

urlpatterns = [
    url(r'^predict', predict, name='predict'),
    url(r'^$', DemoView.as_view(), name='demo'),
]
