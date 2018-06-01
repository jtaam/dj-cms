from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_of_posts, name='list_of_posts'),
	url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
	url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_of_posts_by_category, name='list_of_posts_by_category'),
	url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
	url(r'^post/new/$', views.new_post, name='new_post'),
]