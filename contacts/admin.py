from django.contrib import admin

from .models import Contact, ContactOwner

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25
    
class ContactOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactOwner, ContactOwnerAdmin)