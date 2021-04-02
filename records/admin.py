from django.contrib import admin
from .models import ExpenseCategory, Expense, RevenueCategory, Revenue
from import_export import resources
from import_export.admin import ExportMixin

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


# django-import-export

class ExpenseResource(resources.ModelResource):
    class Meta:
        model = Expense
        fields = ('unit__title','date','category__category','vendor','amount','note')

class RevenueResource(resources.ModelResource):
    class Meta:
        model = Revenue
        fields = ('unit__title','date','category__category','guest','amount','note')


class ExpenseAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ExpenseResource # enable export button
    list_display = ('id','unit','date', 'category', 'vendor', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Expense, ExpenseAdmin)

class RevenueAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RevenueResource # enable export button
    list_display = ('id','unit','date', 'category', 'guest', 'amount', 'note')
    list_display_links =('id',)
    list_filter=('unit','category')
    search_fields=('unit','category')
    list_per_page=25

admin.site.register(Revenue, RevenueAdmin)
