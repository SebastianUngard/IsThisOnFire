from django.db import models

# Create your models here.
class Image(models.Model):
	url = models.CharField(max_length=512)
	is_fire = models.IntegerField(default=0)
	is_training = models.IntegerField(default=1)

class ImageUpload(models.Model):
	img = models.ImageField(upload_to='images/')