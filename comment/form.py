from django import forms
from .models import Comment

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content' : forms.Textarea(attrs={"class": "form-control", 'rows':2,}),
        }
