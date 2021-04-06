from django.db import models

class WeavedImage(models.Model):
    image_name = models.CharField(max_length=60)
    image_source = models.ImageField(upload_to='user_images/',)
    image_url = models.URLField()
    image_description = models.CharField(max_length=60)
    image_creation_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.image_url

class Gallery(models.Model):
    weaved_images = models.ForeignKey(WeavedImage, on_delete=models.CASCADE)
    gallery_name = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=60)
    gallerys = models.ManyToManyField(Gallery)
    def __str__(self):
        return self.username