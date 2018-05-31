from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# category
class Category(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique=True)
	class Meta:
		ordering = ['name']
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('blog:list_of_posts_by_category', args=[self.slug])

	def __str__(self):
		return self.name

# post
class Post(models.Model):
	STATUS_CHOICES = (
			('draft','Draft'),
			('published','Published'),
		)
	title = models.CharField(max_length=250)
	category = models.ForeignKey(Category)
	slug = models.SlugField(max_length=250, unique=True)
	content = models.TextField()
	seo_title = models.CharField(max_length=250)	
	seo_descripttion = models.CharField(max_length=160)
	author = models.ForeignKey(User, related_name='blog_posts')
	published = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.slug])

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments')
	user = models.CharField(max_length=250)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	def approved(self):
		self.approved = True
		self.save()

	def get_absolute_url(self):
		return reverse('blog:add_comment', args=[self.slug])

	def __str__(self):
		return self.user