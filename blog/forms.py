from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # Meta contians info of the model we are going to use
    class Meta:
        model = Post
        fields = ('title', 'text',)