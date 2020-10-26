from os import execl
from django import forms
from .models import Reservation, Comment


class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        exclude = ['user',]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['reservation', 'user',]