from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    """ This class creates a form for a post """

    class Meta:
        """ defining fields for the post """

        model = BlogPost
        fields = ['title', 'text']
        labels = {'title':'', 'text':''}
        widgets = {
            'title':forms.TextInput(attrs={
                'placeholder':'Enter Title ...'
            }),
            'text':forms.Textarea(attrs={
                'cols':90,
                'placeholder':'Enter Post ...',
            })
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control text-bg-light'


