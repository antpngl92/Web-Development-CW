from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# Create your views here.
from django.shortcuts import render
from .models import News, Category



# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        news = News.objects.all()
        context = {'news':news, 'title': 'News'}
        return render(request, 'news/news.html', context)
    else:
        context = {}
        return redirect('logout')
