from django.contrib import admin
from .models import Category, News

class PlaceAdminNews(admin.ModelAdmin):
    list_display = ['title', 'category', 'date']

class PlaceInLineNews(admin.TabularInline):
    model = News
    
class PlaceAdminCategory(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_editable = ['parent']

class PlaceInLineCategory(admin.ModelAdmin):
    model = Category

# Register your models here.
admin.site.register(Category,PlaceAdminCategory)
admin.site.register(News, PlaceAdminNews)