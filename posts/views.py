from django.shortcuts import render


def post_index(request):
    return render(request, 'posts/index.html')
