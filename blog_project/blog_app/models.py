from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    # title contains max 100 symbols
    title = models.CharField(max_length=100)
    # short description
    description = models.CharField(max_length=250)
    # upload_to contains folder where images will be uploaded
    date = models.DateField(default=timezone.now)