from django.contrib import admin
from comment.models import Comment
from django.contrib.auth.admin import UserAdmin

class PlaceAdminComment(admin.ModelAdmin):
    list_display = ['article', 'account', 'publish']

class PlaceInLine(admin.TabularInline):
    model = Comment

admin.site.register(Comment, PlaceAdminComment)
