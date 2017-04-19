from django.contrib import admin

from .models import HealthCenterBlock, HealthCenter, HealthBlog
# Register your models here.

admin.site.register(HealthCenterBlock)
admin.site.register(HealthCenter)
admin.site.register(HealthBlog)
