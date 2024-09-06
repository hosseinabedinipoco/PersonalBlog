from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    is_Admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)