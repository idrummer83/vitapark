from django.db import models

# Create your models here.

class Hotels(models.Model):
    hotel_name = models.CharField('hotel_name', max_length=100)

    class Meta:
        verbose_name = 'main hotel name'
        verbose_name_plural = 'main hotels name'

    def __str__(self):
        return self.hotel_name


class Rooms(models.Model):
    room_hotel_name = models.ForeignKey('Hotels', max_length=100)
    room_category = models.CharField('room_name', max_length=100)
    room_building = models.CharField('room_building', max_length=100)
    room_num = models.CharField('number_of_rooms', max_length=10)
    room_price = models.CharField('room_price', max_length=10)
    room_include = models.TextField('room_include', max_length=1000)
    room_img = models.ImageField(upload_to='room_img', null=True, blank=True)

    class Meta:
        verbose_name = 'room name'
        verbose_name_plural = 'room name'

    def __str__(self):
        return self.room_category


class Gallery(models.Model):
    gallery_name = models.ForeignKey('Hotels', max_length=100)
    gallery_image = models.ImageField(upload_to='hotel_gallery')

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'gallery'

    def __str__(self):
        return 'img'


class Stock(models.Model):
    stock_h_name = models.ForeignKey('Hotels', max_length=100)
    stock_name = models.CharField('stock_name', max_length=100)
    stock_description = models.TextField('stock_name', max_length=1000)
    stock_img = models.ImageField(upload_to='stock_image')
    stock_both = models.NullBooleanField(null=True)

    class Meta:
        verbose_name = 'stock'
        verbose_name_plural = 'stock'

    def __str__(self):
        return self.stock_h_name


class Contacts(models.Model):
    contact_name = models.ForeignKey('Hotels', max_length=100)
    contact_header = models.CharField('contact head', max_length=100)
    contact_adress = models.CharField('contact_name', max_length=100)
    contact_phone = models.CharField('contact_name', max_length=1000)
    contact_email = models.CharField('contact_email', max_length=100)
    contact_map = models.CharField('contact_map', max_length=100)
    contact_description = models.TextField('contact_description', max_length=100)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contact'

    def __str__(self):
        return self.contact_header


class Feedback(models.Model):
    feedback_name = models.CharField('hotel_name', max_length=100)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return self.feedback_name


class RestaurantBars(models.Model):
    r_b_name = models.ForeignKey('Hotels', max_length=100)
    r_b_header = models.CharField('hotel_name', max_length=100)
    restaurant_name = models.CharField('hotel_name', max_length=100)
    bar_name = models.CharField('hotel_name', max_length=100)

    class Meta:
        verbose_name = 'RestaurantBars'
        verbose_name_plural = 'RestaurantBars'

    def __str__(self):
        return self.r_b_header


class ConferenceService(models.Model):
    conf_name = models.ForeignKey('Hotels', max_length=100)
    conf_header = models.CharField('hotel_name', max_length=100)
    conf_description = models.TextField('hotel_name', max_length=100)

    class Meta:
        verbose_name = 'ConferenceService'
        verbose_name_plural = 'ConferenceService'

    def __str__(self):
        return self.conf_header
