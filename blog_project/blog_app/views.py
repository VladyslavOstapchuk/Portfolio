from django.shortcuts import render
from .models import Blog

# Create your views here.

def all_blogs(req):
    # List of all objects
    # blogs = Blog.objects.all()
    # Ordered by publication date. The last 5 publications
    blogs = Blog.objects.order_by('-date')[:5]
    return render(req, 'blog/all_blogs.html', {'blogs':blogs})
