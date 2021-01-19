from django.db import models

class Image(models.Model):
    image_photo = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published')

# Create your models here.
