from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    def __str__(self):
        return f"{self.username}:{self.last_name},{self.first_name}"
        

# Create your models here.
