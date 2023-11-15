from django.urls import path
from . import views

# Links to pages
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]