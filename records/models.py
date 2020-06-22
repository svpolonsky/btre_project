from django.db import models
from datetime import datetime
from listings.models import Listing

class Expense(models.Model):
    categories = [
        ('Utilities - Internet','Utilities - Internet'),
        ('Utilities - Electric','Utilities - Electric'),
        ('Services - Cleaning', 'Services - Cleaning'),
        ('Services - Laundry', 'Services - Laundry'),
        ('Services - Repair', 'Services - Repair'),
        ('Services - Booking', 'Services - Booking'),
        ('Services - Other', 'Services - Other'),
        ('Supplies', 'Supplies'),
        ('Mortgage','Mortgage'),
        ('Tax - Property','Tax - Property'),
        ('Insurance','Insurance'),
        ('Rent','Rent'),
        ('Other', 'Other'),
    ]
    unit = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    date=models.DateTimeField(default=datetime.now)
    category = models.CharField(max_length=200, choices=categories,default='Services - Cleaning')
    vendor = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)

class Revenue(models.Model):
    categories = [
        ('Rent','Rent'),
        ('Other', 'Other'),
    ]
    unit = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    date=models.DateTimeField(default=datetime.now)
    category = models.CharField(max_length=200,choices=categories,default='Rent')
    guest = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)
