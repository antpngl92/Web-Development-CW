from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from django.shortcuts import render
from .models import News, Category
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict, JsonResponse
# Create your views here.
def home(request):
    news = News.objects.all()
    categories = Category.objects.all()

    context = {'news':news, 'categories':categories,'title': 'News'}
    return render(request, 'news/news.html', context)


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