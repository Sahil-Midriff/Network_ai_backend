from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Cuser(AbstractUser):
    phone_no          = models.CharField(max_length=10,unique=True)
    address           = models.TextField()
    age               = models.IntegerField()

    def __str__(self):
        return self.full_name
