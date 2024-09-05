from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    is_Admin = models.BooleanField(default=False)
    