
from django.urls import path
from news.views import (home, get_cat_API)
from .views import *
from newspaper import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',home,name='news_home'),
    path(r'(?P<cat>[A-Za-z]+)/$',home,name='news_home'),
    path('get_news_API/', get_cat_API, name="get_news_api"),
    path('like/', like, name="like"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
