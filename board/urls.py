from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name= 'post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
]
