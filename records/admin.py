from django.contrib import admin
from .models import ExpenseCategory, Expense, RevenueCategory, Revenue
from import_export import fields, resources
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget
from listings.models import Listing

# Categories

class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')
    list_display_links =('id','category')
    list_filter=('category',)
    search_fields=('category',)
    list_per_page=25

admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)

class RevenueCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')
    list_display_links =('id','category')
    list_filter=('category',)
    search_fields=('category',)
    list_per_page=25

admin.site.register(RevenueCategory, RevenueCategoryAdmin)


# django-import-export resources

class ExpenseResource(resources.ModelResource):
    unit = fields.Field(column_name='unit',attribute='unit',widget=ForeignKeyWidget(Listing, 'title'))
    category = fields.Field(column_name='category',attribute='category',widget=ForeignKeyWidget(ExpenseCategory, 'category'))
    class Meta:
        model = Expense
        fields = ('id','unit','date','category','vendor','amount','note')

class RevenueResource(resources.ModelResource):
    unit = fields.Field(column_name='unit',attribute='unit',widget=ForeignKeyWidget(Listing, 'title'))
    category = fields.Field(column_name='category',attribute='category',widget=ForeignKeyWidget(RevenueCategory, 'category'))
    class Meta:
        model = Revenue
        fields = ('id','unit','date','category','guest','amount','note')

# integrate with admin

class ExpenseAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ExpenseResource # enable export & import buttons
    list_display = ('id','unit','date', 'category', 'vendor', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Expense, ExpenseAdmin)

class RevenueAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RevenueResource # enable export & import button
    list_display = ('id','unit','date', 'category', 'guest', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Revenue, RevenueAdmin)
