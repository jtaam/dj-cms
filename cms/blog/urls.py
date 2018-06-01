from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_of_posts, name='list_of_posts'),
	url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
	url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_of_posts_by_category, name='list_of_posts_by_category'),
	url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
	# backend
	url(r'^backend/post/new/$', views.new_post, name='new_post'),
	url(r'^backend/post/$', views.list_of_posts_backend, name='list_of_posts_backend'),
	url(r'^backend/(?P<slug>[-\w]+)/edit/$', views.edit_post, name='edit_post'),
	url(r'^backend/(?P<slug>[-\w]+)/delete/$', views.delete_post, name='delete_post'),
]