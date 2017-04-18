from django.db import models

# Create your models here.

class HotelFamilyClub(models.Model):
    hfc = models.CharField('hotel family club', max_length=100)

    class Meta:
        verbose_name = 'hotel family club'
        verbose_name_plural = 'hotel family club'

    def __str__(self):
        return self.hfc
