from django.db import models

class WeaverUser(models.Model):
    user_id = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length = 254, unique=True)
    def __str__(self):
        return self.email

class WeavedImage(models.Model):
    image_name = models.CharField(max_length=60)
    image_source = models.ImageField(upload_to='user_images/',)
    image_url = models.URLField(blank=True, null=True)
    image_creation_time = models.DateTimeField(auto_now=True)
    weaved_user = models.ForeignKey(WeaverUser, related_name='weaved_images', on_delete=models.CASCADE,  blank=True, null=True)
    def __str__(self):
        return self.image_url

