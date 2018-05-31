from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment # Hookup the model
		fields = ('user', 'email', 'body')
