from django.db import models

# Create your models here.

class HealthCenterBlock(models.Model):
    health_header = models.CharField('health name', max_length=100)

    class Meta:
        verbose_name = 'health_name header'
        verbose_name_plural = 'health_name header'

    def __str__(self):
        return self.health_header


class HealthCenter(models.Model):
    health_name = models.CharField('health name', max_length=100)
    health_description = models.TextField('health description', max_length=1000)

    class Meta:
        verbose_name = 'health_name'
        verbose_name_plural = 'health_name'

    def __str__(self):
        return self.health_name


class HealthBlog(models.Model):
    blog_header = models.CharField('header', max_length=100)
    blog_text = models.TextField('header', max_length=1000)

    class Meta:
        verbose_name = 'Health blog'
        verbose_name_plural = 'Health blog'

    def __str__(self):
        return self.blog_header


class AdditionalService(models.Model):
    addit_serv_header = models.CharField('header', max_length=100)
    addit_serv_text = models.TextField('header', max_length=1000)

    class Meta:
        verbose_name = 'Health blog'
        verbose_name_plural = 'Health blog'

    def __str__(self):
        return self.addit_serv_header
