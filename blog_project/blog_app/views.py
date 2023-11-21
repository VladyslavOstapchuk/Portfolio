from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(req):
    # List of all objects
    # blogs = Blog.objects.all()
    # Ordered by publication date. The last 5 publications
    # blogs = Blog.objects.order_by('-date')[:5]
    blogs = Blog.objects.order_by('-date')
    return render(req, 'blog/all_blogs.html', {'blogs':blogs})

def detail(req, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'blog/detail.html', {'blog':blog})
