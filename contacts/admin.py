from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'name', 'listing', 'email', 'phone', 'message', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')

admin.site.register(Contact, ContactAdmin)
