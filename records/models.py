from django.db import models
from datetime import datetime
from listings.models import Listing

class ExpenseCategory(models.Model):
    category = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Expense Categories"
    
class Expense(models.Model):
    unit = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        name = str(self.unit) + " " + str(self.category)
        return name

class RevenueCategory(models.Model):
    category = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name_plural = "Revenue Categories"
    def __str__(self):
        return self.category


class Revenue(models.Model):
    unit = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(RevenueCategory, on_delete=models.CASCADE)
    guest = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    note = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return str(self.unit) + " " + str(self.category)

