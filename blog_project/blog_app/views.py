from django.shortcuts import render
from .models import Blog

# Create your views here.

def all_blogs(req):
    # Database model
    blogs = Blog.objects.all()

    return render(req, 'blog/all_blogs.html', {'blogs':blogs})
