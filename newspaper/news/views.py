from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import News, Category



# Create your views here.
def home(request):
    news = News.objects.all()
    context = {'news':news, 'title': 'News'}
    return render(request, 'news/news.html', context)
