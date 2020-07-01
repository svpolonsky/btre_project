from django.contrib import admin
from .models import ExpenseCategory, Expense, RevenueCategory, Revenue

class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')
    list_display_links =('id','category')
    list_filter=('category',)
    search_fields=('category',)
    list_per_page=25

admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','unit','date', 'category', 'vendor', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Expense, ExpenseAdmin)

class RevenueCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')
    list_display_links =('id','category')
    list_filter=('category',)
    search_fields=('category',)
    list_per_page=25

admin.site.register(RevenueCategory, RevenueCategoryAdmin)

class RevenueAdmin(admin.ModelAdmin):
    list_display = ('id','unit','date', 'category', 'guest', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Revenue, RevenueAdmin)
