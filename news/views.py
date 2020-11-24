from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from .models import News, Category
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict, JsonResponse, HttpResponse
from account.models import Account
from comment.models import Comment 

def home(request):
    context = {}
    news = News.objects.all()
    if not request.user.is_authenticated:
        categories = Category.objects.all()
        for article in news:
            article.likes = article.users.all().count()
            article.save()
        context = {'news':news, 'categories':categories,'title': 'News'}
    else:
        user_favourite_cat = request.user.favourite.all()
        news = News.objects.filter(category=user_favourite_cat)
        news_comments = Comment.objects.prefetch_related('article').all()
        context = {
            'news':news, 
            'categories':user_favourite_cat,
            'comments' : news_comments,
            'title': 'News',
            }
    return render(request, 'news/news.html', context)

def article_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        article = News.objects.get(pk=pk)
        comments = Comment.objects.filter(article=article)
        context = {
            'article' : article,
            'comments': comments,
            'title' : 'Article'
        }
    return render(request, 'news/article.html', context)


@csrf_exempt
def like(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        user = request.user
        pk = pk
        likedArticles = user.likes.all()
        print(likedArticles)
        article = News.objects.get(pk=pk)
        if article in likedArticles:
            user.likes.remove(article)
        else:
            user.likes.add(article)
        article.likes = article.users.all().count()
        article.save()
        user.save()

        return JsonResponse({'currentLikes': article.likes}, status=200)

@csrf_exempt
def get_cat_API(reqest):
    if reqest.method == "GET":
        data = Category.objects.all()
        serialized_object = serializers.serialize('python', data)
        return JsonResponse(serialized_object, safe=False)

@csrf_exempt
def get_cat_API(reqest):
    if reqest.method == "GET":
        data = Category.objects.all()
        serialized_object = serializers.serialize('python', data)
        return JsonResponse(serialized_object, safe=False)
    if request.method == "POST":
        news = request.POST.getlist('cat')
        print(news)
