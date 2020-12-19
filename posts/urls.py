from django.urls import path

from .views import post_index

app_name = 'posts'

urlpatterns = [
    path('', post_index, name='index'),
]
