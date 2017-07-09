from django import forms
from .models import FeedBackMessage


class FeedBackMessageFrom(forms.ModelForm):
    class Meta:
        model = FeedBackMessage

    search_fields = ['name', 'email', ]
