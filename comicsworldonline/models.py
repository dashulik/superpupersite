from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.CharField(max_length=100, null=True)