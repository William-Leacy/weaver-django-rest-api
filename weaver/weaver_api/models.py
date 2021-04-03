from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=60)
    def __str__(self):
        return self.username