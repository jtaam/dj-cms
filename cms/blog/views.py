from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def list_of_posts(request):
	# posts = Post.objects.all()
	posts = Post.objects.filter(status='published')
	template = 'blog/post/list_of_posts.html'
	context = {'posts':posts}
	return render(request, template, context)


def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	template = 'blog/post/blog_post.html'
	context = {'post':post}
	return render(request, template, context)