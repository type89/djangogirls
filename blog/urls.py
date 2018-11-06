from django.conf.urls import include, url
from . import views
from django.contrib import admin
#from django.urls import path
from django.urls import include, path


admin.site.site_header = 'Neo-momopi-blog管理コンソール' 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
]


"""
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
"""
