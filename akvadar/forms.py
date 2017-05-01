from django import forms
from django.core.exceptions import ValidationError

def name_validator(name):
    if not name.startswith('Mr. '):
        raise ValidationError('only for men')
    return name


class Feedbackform(forms.Form):
    feedback = forms.CharField(label='otziv', widget=forms.Textarea())
    nick = forms.CharField(label='name', validators=(name_validator,))
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    def clean_feedback(self):
        if 'win' in self.cleaned_data('feedback').lower():
            raise forms.ValidationError('win is in form')
        return self.cleaned_data['feedback']
