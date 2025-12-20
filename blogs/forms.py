from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    """ This class creates a form for a post """

    class Meta:
        """ defining fields for the post """

        model = BlogPost
        fields = ['title', 'text']
        labels = {'title':'Enter title', 'text':'Type Post'}
        widget = {'text':forms.Textarea({'cols':70})}