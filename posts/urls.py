from django.urls import path

from .views import PostView, user_posts, create_post

app_name = 'posts'

urlpatterns = [
    path('', PostView.as_view(), name='index'),
    path('posts/<int:pk>/', user_posts, name='user_posts'),
    path('post/create/', create_post, name='create')
]
