from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text='Required. Add username')
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    dob = forms.DateField(help_text='Required. Add your date of birth',widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))


    class Meta:
        model = Account
        fields = ('username', 'email', 'dob', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')
    
    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Invalid login')
        