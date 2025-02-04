from django.urls import path
from .views import get_posts
from .views import create_posts

from . import views

urlpatterns = [ 
               path("", views.index, name="index"),
               path('posts/', views.get_posts, name='get_posts'),
               path('posts/create/', views.create_posts, name='create_posts')
               ]

