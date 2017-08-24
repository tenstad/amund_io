from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from .views import Index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tags/', include('tags.urls')),
    url(r'^files/', include('files.urls')),
    url(r'^article/', include('articles.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^numclass/', include('numclass.urls')),
    url(r'^$', Index.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
