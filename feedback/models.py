from django.db import models
from main.models import Hotel

# Create your models here.


class Feedback(models.Model):
    # hotel = models.ForeignKey(Hotel)
    feedback = models.TextField('Отзыв')
    nick = models.CharField('Имя', max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return "Feedback {}".format(self.nick)
