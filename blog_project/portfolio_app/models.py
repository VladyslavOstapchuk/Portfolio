from django.db import models

# Create your models here.

# Description of database table
class Project(models.Model):
    # title contains max 100 symbols
    title = models.CharField(max_length=100)
    # short description
    description = models.CharField(max_length=250)
    # upload_to contains folder where images will be uploaded
    image = models.ImageField(upload_to='portfolio_app/images/')
    # url to 
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title