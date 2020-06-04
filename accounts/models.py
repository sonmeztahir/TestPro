from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	sinif = models.CharField(max_length=3, verbose_name='Sınıfı')
	numara = models.CharField(max_length=5, verbose_name='Numarası')
	