from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_of_posts, name='list_of_posts'),
	url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail')
]