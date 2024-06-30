from django.db import models
from django.urls import reverse

site_type =(
    ('Online Learning', 'Online Learning'),
    ('E-Commerce', 'E-Commerce')
)

class Project_Rezome(models.Model):
    title = models.CharField(max_length=50)
    sit_type = models.CharField(max_length=50, choices= site_type)
    site_cover = models.ImageField(upload_to="covers/", blank=True)
    site_linke = models.CharField(max_length=250)


    def __str__(self):
        return self.title
    
