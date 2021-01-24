from django.db import models

class Image(models.Model):
    # name = models.CharField(max_length=50)
    image_photo = models.ImageField(upload_to='upload/')
    # pub_date = models.DateTimeField('date published')
# Create your models here.
