from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulli', 'teksti']
        widgets = {
            'titulli': forms.TextInput(attrs={'class': 'form-control'}),
            'teksti': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['komenti', 'post']
        widgets = {
            'post': forms.HiddenInput(),
            'komenti': forms.Textarea(attrs={'class': 'form-control'})
        }
