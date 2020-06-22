from django.contrib import admin
from .models import Expense, Revenue

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','unit','date', 'category', 'vendor', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Expense, ExpenseAdmin)

class RevenueAdmin(admin.ModelAdmin):
    list_display = ('id','unit','date', 'category', 'guest', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Revenue, RevenueAdmin)
