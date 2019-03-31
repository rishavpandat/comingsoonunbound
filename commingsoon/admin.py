from django.contrib import admin

from .models import SoonModel

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'business_name', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email',)
  list_per_page = 25

admin.site.register(SoonModel, ContactAdmin)


