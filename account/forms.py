from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text='Required. Add username')
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    dob = forms.DateField(help_text='Required. Add your date of birth',widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}), label='Date of Birth')


    class Meta:
        model = Account
        fields = ('username', 'email', 'dob', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')
    
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid login')


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'favourite', 'profile_picture')


    # Make sure that the username and email that user try to change to is not already registered in the DataBase
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError(f"Username: {account.username} is already in use.")
    
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError(f"Email: {account.email} is already in use.")


