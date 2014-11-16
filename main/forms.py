from django import forms
from main.models import Post

class NewPostForm(forms.Form):
    title = forms.CharField(label='Subject', max_length=255)
    body = forms.CharField(widget=forms.Textarea, label='Content')

class AnotherPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')