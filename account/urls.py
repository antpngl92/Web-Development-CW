
from django.urls import path
from account.views import (registration_view,logout_view, login_view, account_view)

urlpatterns = [
    path('register/',registration_view,name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/',login_view,name='login'),
    path('update', account_view, name='account'),
]