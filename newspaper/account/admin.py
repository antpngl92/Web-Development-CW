from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'dob', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'email') # Fields for searching in the admin panel
    readonly_fields = ('date_joined', 'last_login') # fields that cannot be updated in admin control panel

    # Those fields are requered, otherwise throws an error
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)