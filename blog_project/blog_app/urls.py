from django.urls import path
from . import views

app_name = 'blog'

# Links to pages
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # Allows to create unique links to every blog post
    path('<int:blog_id>/', views.detail, name='detail'),
]