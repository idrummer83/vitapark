from django.db import models

# Create your models here.

class Feedback(models.Model):
    feedback_name = models.CharField('hotel_name', max_length=100)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return self.feedback_name
