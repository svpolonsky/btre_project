from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Owner(models.Model):
    STATUS_CHOICES = (
        ('Prospect', 'Prospect'),
        ('Customer', 'Customer'),
        ('Retired', 'Retired'),
    )
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='Prospect')
    name = models.CharField(max_length=200)
    #user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True) 
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True) 
    #photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    account = models.CharField(max_length=200, blank=True)
    client_since=models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

