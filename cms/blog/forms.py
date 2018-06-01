from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment # Hookup the model
		fields = ('user', 'email', 'body')


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content', 'category', 'seo_title', 'seo_descripttion','status')

