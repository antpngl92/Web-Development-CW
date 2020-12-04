from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict, JsonResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import os
from django.contrib.auth.decorators import login_required


def registration_view(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        return redirect('news_home')
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            account = authenticate(username=username,  password=raw_password)
            login(request, account)
            send_mail('Registration Complete', 'Congratulations ' + username + '! You have successfully registered for our coursework project application! This email serves only to let you know that Part A2 of the Advanced requirements works!', 'newspapergroup43@gmail.com', [email])
            return redirect('news_home')
        else:
            context['registration_form'] = form
    else: # if GET req. user visits the page for first rime, meaning they would like to register
        form = RegistrationForm()
        context['registration_form'] = form
        context['title'] = 'Register'
    return render(request, 'account/register.html', context )


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('news_home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('news_home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    context['title'] = 'Login'

    return render(request, 'account/login.html', context)


def delete_picture_API(request, id):
    user = request.user
    current_image = user.profile_picture
    current_image.delete()
    image = "profilePic/pp.png"
    user.profile_picture = image
    user.save()
    return JsonResponse({'status':'Deleted!'})


@login_required
def account_view(request):
    context = {}
    categories = request.user.favourite.all()
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = AccountUpdateForm(
            initial = {
                'username' : request.user.username,
                'email' : request.user.email,
                'dob' : request.user.dob,
                'favourite' : request.user.favourite.all(),
                'profile_picture' : request.user.profile_picture
            }
        )
    context['account_form'] = form
    return render(request, 'account/account.html', context)
