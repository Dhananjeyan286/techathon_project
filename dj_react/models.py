from django.db import models

# Create your models here.
class user(models.Model):
    email_id = models.EmailField(max_length=55,primary_key=True)
    name = models.CharField(max_length=55)
    password = models.CharField(max_length=1000)
    admin = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    normal = models.BooleanField(default=False)