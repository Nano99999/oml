from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    is_use = models.BooleanField(default=True)

 