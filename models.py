from django.db import models
from django.utils import timezone

class todo(models.Model):
	description=models.CharField(max_length=160)
	deadline= models.DateTimeField(default=timezone.now)
	progress=models.CharField(max_length=10)

# Create your models here.
