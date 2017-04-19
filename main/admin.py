from django.contrib import admin

from .models import Hotel, Room, Gallery, Stock, Contacts, AdditionalService
# Register your models here.

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Gallery)
admin.site.register(Stock)
admin.site.register(Contacts)
admin.site.register(AdditionalService)
