from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Adduser(models.Model):

    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
