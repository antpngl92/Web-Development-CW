from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin

admin.site.register(Account)