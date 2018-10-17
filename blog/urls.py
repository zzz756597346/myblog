from django.conf.urls import url
from . import views
from django.urls import path,include,re_path

app_name='blog'

urlpatterns = [
    url('^index/$', views.index,name='index'),
    re_path('^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    re_path('^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url('^edit/action/$', views.edit_action,name='edit_action'),
    url('^edit/del_action', views.del_action, name='del_action'),
]
