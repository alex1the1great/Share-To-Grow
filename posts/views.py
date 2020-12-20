from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Post


class PostView(ListView):
    template_name = 'posts/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:10]


def user_posts(request, pk):
    posts = Post.objects.filter(author_id=pk).order_by('-pub_date')
    return render(request, 'posts/user_posts.html', {'user_posts': posts})
