from django.urls import path
from .views import *

urlpatterns = [
    path('',BlogList.as_view(),name='blog_list'),
    path('create/',CreatePost.as_view(),name='c'),
    path('read/<slug>/',Read,name='r'),
    path('liked_post/<pk>/',liked_post,name='liked_post'),
    path('unliked_post/<pk>/',unliked_post,name='unliked_post'),
    path('myall/',UserBlogs.as_view(),name='user_blogs'),
    path('editBlog/<pk>',UpdateBlog.as_view(),name='upateBlog'),
    path('BlogDelete/<pk>',BlogDeleteView.as_view(),name='bd')

]