from django.views.generic import ListView

from .models import Post


class PostView(ListView):
    template_name = 'posts/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:10]
