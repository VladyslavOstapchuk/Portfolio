from django.shortcuts import render
from .models import Project

# Create your views here.
def home(req):
    # Import of all data from DB
    projects = Project.objects.all()

    return render(
    # Request
    req,
    # Path to html page template. Path should not contain template folder name
    'portfolio/home.html', {
    # Passing DB objects to the html template
    'projects':projects})