
from django.urls import path
from news.views import (home) #get_cat_API
from .views import *
from newspaper import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('' ,home, name='news_home'),
    path('like/<int:pk>/', like, name="like"),
    path('article/<int:pk>/', article_view, name='article'),
    path('comment', new_comment_api, name='new comment'),
    path('delete/comment/<int:pk>/', delete_comment_api, name='delete comment'),
    path('edit/comment/<int:pk>/', edit_comment_api, name='edit comment'),
    path('reply/comment/<int:pk>/', reply_comment_api, name='reply comment'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
