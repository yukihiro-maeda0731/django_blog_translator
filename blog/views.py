from django.shortcuts import render

from blog.models import Post

# Create your views here.

class BlogView:
    model = Post
    template_name = 'blog.heml'
