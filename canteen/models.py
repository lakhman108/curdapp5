from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # address = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    
class items(models.Model):
    item_name = models.CharField(max_length=255, blank=False, null=False, )