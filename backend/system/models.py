from django.db import models

# Create your models here.
class ConfigParams(models.Model):
    param_name = models.CharField(max_length=128)
    param_value = models.CharField(max_length=1024)