from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=60)
    def __str__(self):
        return self.username

class Gallery(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    name = models.CharField(max_length=50, default='Gallery ')

class WeavedImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=60)
    image_source = models.ImageField(upload_to='user_images/', default='image')
    image_url = models.URLField()
    image_description = models.CharField(max_length=60)
    image_creation_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.image_url
