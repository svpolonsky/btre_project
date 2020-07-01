from django.contrib import admin

from .models import Owner

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'client_since')
    list_display_links=('id','name')
    search_fields=('name',)
    list_per_page=25

admin.site.register(Owner, OwnerAdmin)

