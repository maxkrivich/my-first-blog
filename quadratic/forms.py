from django import forms

class QuadraticFrom(forms.Form):
    a = forms.FloatField(label='A koeff')
    b = forms.FloatField(label='B koeff')
    c = forms.FloatField(label='C koeff')
