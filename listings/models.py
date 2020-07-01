from django.db import models
from datetime import datetime
from realtors.models import Realtor
from owners.models import Owner

class Listing(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='Inactive')
    realtor = models.ForeignKey(
        Realtor, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    # primary
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    # other
    #owner = models.ManyToManyField(Owner)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft=models.IntegerField() # depreciated
    m2_total=models.IntegerField(default=0) # new
    floor=models.IntegerField(default=0) # new
    parking = models.CharField(max_length=100, default='') # new
    lot_size=models.DecimalField(max_digits=5,decimal_places=1) # depreciated
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title