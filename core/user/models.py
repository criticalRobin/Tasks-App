from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    image = models.ImageField(upload_to="users/img", null=True, blank=True)

    def __str__(self):
        return self.username
