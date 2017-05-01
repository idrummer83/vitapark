from django import forms
from .models import Hotel
from django.core.exceptions import ValidationError


# def name_validator(name):
#     if not name.startswith('Mr.'):
#         raise ValidationError('Only for men')
#     return name


class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Отзыв', help_text='help', widget=forms.Textarea())
    # nick = forms.CharField(label='Имя', validators=(name_validator,))
    nick = forms.CharField(label='Имя',)
    # hotel = forms.ChoiceField(label='hotel', widget=forms.Select(),choices = ([('1','akvadar'), ('2','borisfen'), ]), initial='1', required = True,)

    def clean_feedback(self):
        if 'windows' in self.cleaned_data['feedback'].lower():
            raise ValidationError('Windows is in form')
        return self.cleaned_data['feedback']
