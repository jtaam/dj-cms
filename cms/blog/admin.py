from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','slug','author','published','status','created','updated']
	class Meta:
		Post

admin.site.register(Post, PostAdmin)