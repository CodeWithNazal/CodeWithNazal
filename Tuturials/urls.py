from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('tutorials/', views.tutorials, name='tutorials'),
    path('tutorial/<str:tutorial_title>', views.tutorial, name='tutorial'),
    path('tutorial/<str:tutorial_title>/<str:chapter_title>', views.chapter, name='chapter'),
    path('code/<str:tutorial_title>', views.source_code, name='source-code'),
    path('create-tutorial', views.create_tutorial, name='create-tutorial'),
    path('create-chapter', views.create_chapter, name='create-chapter'),

    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:blog_title>', views.blog, name='blog'),
    path('create-blog', views.create_blogcontent, name='create-blogcontent'),

    path('news/', views.news_all, name='news_all'),
    path('news/<str:news_title>', views.news_instance, name='news_instance'),
    path('create_news', views.create_news, name='create-news'),

    path('searched/', views.searched, name='searched'),

    path('youtube-in-python', views.promotion, name='promotion')
]


"""
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:blog_title>', views.blog, name='blog'),

    path('news/', views.news_all, name='all_news'),
    path('news/<str:news_title>', views.news_instance, name='single_news')
"""