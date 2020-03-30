from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulli', 'teksti']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['komenti', 'post']
        widgets = {
            'post': forms.HiddenInput()
        }
