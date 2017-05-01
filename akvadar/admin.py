from django.contrib import admin

from .models import HealthCenter, HealthService
# Register your models here.

@admin.register(HealthCenter)
class HealthCenterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



# admin.site.register(HealthCenter)
admin.site.register(HealthService)
