from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from .models import News, Category
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict, JsonResponse, HttpResponse, HttpResponseRedirect
from account.models import Account
from comment.models import Comment 
from comment.form import NewCommentForm


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
        context = {}
        article = News.objects.get(pk=pk)
        comments = Comment.objects.filter(article=article)
        context = {'article': article, 'comments': comments, 'title': 'Article'}
    return render(request, 'news/article.html', context)


@csrf_exempt
def reply_comment_api(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        articleID = request.POST['article_id']
        article = News.objects.get(pk=articleID) # Get the Article object
        comment_content = request.POST['content']
        comment = Comment.objects.get(pk=pk) # Get the comment object 
        child_comment = Comment(article=article, parent=comment, account=request.user, content=comment_content) # Create new child comment 
        child_comment.save()
        child_comment_id = child_comment.pk
        child_comment_date = child_comment.publish
        data = []
        data.append(child_comment_id)
        data.append(child_comment_date)
    return JsonResponse(data, safe=False) 



@csrf_exempt        
def new_comment_api(request):
    if request.method == "POST" and request.user.is_authenticated:
        articleID = request.POST['article_id']
        article = News.objects.get(pk=articleID)
        content = request.POST['content']
        comment = Comment(article=article, account=request.user, content=content )
        comment.save()
        new_comment_id = comment.pk
        new_comment_date = comment.publish
        data = []
        data.append(new_comment_id)
        data.append(new_comment_date)
    return JsonResponse(data, safe=False)

@csrf_exempt
def edit_comment_api(request, pk):
    if request.method == "PUT" and request.user.is_authenticated:
        data = QueryDict(request.body)
        comment_content = data['content']
        article_pk = data['article_id']
        article = News.objects.get(pk=article_pk)

        comment_date = Comment.objects.get(pk=pk)
        comment_date = comment_date.publish
        
        comment = Comment(pk=pk, article=article, account=request.user, content=comment_content, publish=comment_date)
        comment.save()
    return JsonResponse({'status': 'Saved'})


@csrf_exempt
def delete_comment_api(request, pk):
    if request.method == "DELETE" and request.user.is_authenticated:
        comment = Comment.objects.get(pk=pk)
        comment.delete()
    return JsonResponse("success", safe=False)    


@csrf_exempt
def like(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        user = request.user
        likedArticles = user.likes.all()
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
