from django import forms
from .models import Document, post, Comment, Profile


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title', 'content', 'categories', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']