from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import CreatePostForm


class PostView(ListView):
    template_name = 'posts/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:10]


def user_posts(request, pk):
    posts = Post.objects.filter(author_id=pk).order_by('-pub_date')
    username = User.objects.get(pk=pk)
    return render(request, 'posts/user_posts.html', {'user_posts': posts, 'username': username})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:index')
    else:
        form = CreatePostForm()
    return render(request, 'posts/create_post.html', {'form': form})
