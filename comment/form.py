from django import forms
from .models import Comment
from mptt.forms import TreeNodeChoiceField

class NewCommentForm(forms.ModelForm):
    # This is utilised if there is a parent comment that we want to connect to 
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].required = False
        self.fields['parent'].label = ''
        self.fields['parent'].widget.attrs.update( # Hide the parent selector
            {'class':'d-none'}
        )

    class Meta:
        model = Comment
        fields = ['content', 'parent']
        widgets = {
            'content' : forms.Textarea(attrs={'class': 'ml-3 mb-3 form-control border-0 comment-add rounded-0', 'rows':1, 'placeholder' : 'Add a comment'}),
        }
