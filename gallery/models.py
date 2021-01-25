from django.db import models

class Image(models.Model):
    image_photo = models.ImageField(upload_to='upload/')
    # name = models.CharField(max_length=50)
    # pub_date = models.DateTimeField('date published')
