from django.contrib import admin

from .models import HealthCenter, HealthService, PaidServices, Services, ServicesInclude
# Register your models here.

@admin.register(HealthCenter)
class HealthCenterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ServicesIncludeAdmin(admin.TabularInline):
    model = ServicesInclude


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    inlines = [
        ServicesIncludeAdmin,
    ]


admin.site.register(HealthService)
admin.site.register(PaidServices)
