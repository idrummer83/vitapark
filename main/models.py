from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField('hotel_name', max_length=50)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return self.name


# class Mymanager(models.Model):
#     def zzz(self):
#         return super().zzz().filter(price__gt==234)
#     def set_price(self, k):
#         super().zzz().update(price=F('price')*k)


class Room(models.Model):
    hotel = models.ForeignKey('Hotel')
    category = models.CharField('room_name', max_length=100)
    apartament = models.CharField('room_building', max_length=100)
    room_quantity = models.SmallIntegerField('number_of_rooms')
    price = models.DecimalField('room_price', decimal_places=1, max_digits=100000, max_length=10, null=True, blank=True)
    inclusive = models.TextField('room_include', max_length=1000)
    # img = models.ForeignKey('Gallery')
    # objects = Mymanager()

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return self.category
    # def getPrice(self):
    #     return "{} grn".format(self.price)


class Gallery(models.Model):
    image_name = models.CharField('img name', max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='hotel_gallery', blank=True, null=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return 'Галлерея'


class Stock(models.Model):
    hotels = models.ManyToManyField('Hotel', blank=True)
    name = models.CharField('name', max_length=100)
    description = models.TextField('description', max_length=1000)
    # stock_img = models.ForeignKey('Gallery', blank=True)
    stock_both = models.NullBooleanField(null=True)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name


class Contacts(models.Model):
    # contact_name = models.ForeignKey('Hotel', max_length=100)
    hotel = models.OneToOneField('Hotel')
    header = models.CharField('header', max_length=100)
    adress = models.CharField('adress', max_length=100)
    phone = models.PositiveIntegerField('phone')
    email = models.EmailField('contact_email', max_length=100)
    map = models.CharField('contact_map', max_length=100)
    description = models.TextField('contact_description', max_length=100)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.header


class AdditionalService(models.Model):
    hotel = models.ForeignKey('Hotel', max_length=100)
    name = models.CharField('name', max_length=100)
    short_description = models.TextField('hotel_name')
    description = models.TextField('hotel_name')
    img = models.ForeignKey('Gallery')

    class Meta:
        verbose_name = 'Дополнительные услуги'
        verbose_name_plural = 'Дополнительные услуги'

    def __str__(self):
        return self.name
