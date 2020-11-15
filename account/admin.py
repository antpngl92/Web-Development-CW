from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin

class PlaceAdminAccount(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_admin', 'last_login']
    list_editable = ['is_admin']

class PlaceInlIne(admin.TabularInline):
    model = Account


admin.site.register(Account,PlaceAdminAccount)