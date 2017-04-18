from django.contrib import admin

from .models import Hotels, Rooms, Gallery, Stock, Contacts, Feedback, RestaurantBars, ConferenceService
# Register your models here.

admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Gallery)
admin.site.register(Stock)
admin.site.register(Contacts)
admin.site.register(Feedback)
admin.site.register(RestaurantBars)
admin.site.register(ConferenceService)
