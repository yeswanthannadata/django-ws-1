from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
