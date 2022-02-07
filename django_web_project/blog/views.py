from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'posts_list.html'


