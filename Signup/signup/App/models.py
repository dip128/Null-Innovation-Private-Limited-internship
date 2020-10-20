from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class extendeduser(models.Model):
    organization=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
         return self.user.email