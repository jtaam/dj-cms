from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def list_of_posts_by_category(request, category_slug):
	categories = Category.objects.all()
	posts = Post.objects.filter(status='published')
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		posts = posts.filter(category=category)
	template = 'blog/category/list_of_posts_by_category.html'
	context = {'categories': categories, 'posts':posts, 'category':category}
	return render(request, template, context)


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