from django.contrib import admin
from comment.models import Comment
from django.contrib.auth.admin import UserAdmin
from mptt.admin import MPTTModelAdmin



admin.site.register(Comment, MPTTModelAdmin)
