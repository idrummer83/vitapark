from django.db import models

# Create your models here.

class HealthCenter(models.Model):
    name = models.CharField('health service', max_length=100)
    slug = models.SlugField(verbose_name='link', unique=True)

    class Meta:
        verbose_name = 'health center service name'
        verbose_name_plural = 'health center service name'

    def __str__(self):
        return self.name


# class HealthService(models.Model):
class HealthService(HealthCenter):
    # service = models.ForeignKey('HealthCenter')
    hs_name = models.CharField('service name', max_length=100)
    short = models.CharField('short description', max_length=500)
    description = models.TextField('full description')

    class Meta:
        verbose_name = 'health_name'
        verbose_name_plural = 'health_name'

    def __str__(self):
        return self.name


class Feedback(models.Model):
    # hotel = models.ForeignKey('Hotel')
    feedback = models.TextField('asd')
    nick = models.CharField('name', max_length=12)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Feedback {}".format(self.nick)


class PaidServices(models.Model):
    name = models.CharField('paid services', max_length=200)
    class Meta:
        verbose_name = 'платные услуги'
        verbose_name_plural = 'платные услуги'

    def __str__(self):
        return self.name


class Services(models.Model):
    ps = models.ForeignKey('PaidServices', blank=True, on_delete=models.CASCADE)
    name = models.CharField('hz service', max_length=200)
    class Meta:
        verbose_name = 'услуги2'
        verbose_name_plural = 'услуги2'

    def __str__(self):
        return self.name


class ServicesInclude(models.Model):
    ps = models.ForeignKey('PaidServices', blank=True)
    head = models.ForeignKey('Services', blank=True)
    name = models.CharField('name service', max_length=200)
    time = models.SmallIntegerField('Durability')
    price = models.SmallIntegerField('price')
    class Meta:
        verbose_name = 'услуги3'
        verbose_name_plural = 'услуги3'

    def __str__(self):
        return self.name

class PaidServices(models.Model):
    name = models.CharField('paid services', max_length=200)
    class Meta:
        verbose_name = 'платные услуги'
        verbose_name_plural = 'платные услуги'

    def __str__(self):
        return self.name


class Services(models.Model):
    ps = models.ForeignKey('PaidServices', blank=True, on_delete=models.CASCADE)
    name = models.CharField('hz service', blank=True, max_length=200)
    class Meta:
        verbose_name = 'услуги2'
        verbose_name_plural = 'услуги2'

    def __str__(self):
        return self.name


class ServicesInclude(models.Model):
    head = models.ForeignKey('Services', blank=True)
    name = models.CharField('name service', max_length=200)
    time = models.CharField('Durability', max_length=100)
    price = models.SmallIntegerField('price')
    class Meta:
        verbose_name = 'услуги3'
        verbose_name_plural = 'услуги3'

    def __str__(self):
        return self.name
