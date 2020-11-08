
from django.urls import path
from news.views import (home, get_cat_API)

urlpatterns = [
    path('',home,name='news_home'),
    path('get_news_API/', get_cat_API, name="get_news_api"),
]