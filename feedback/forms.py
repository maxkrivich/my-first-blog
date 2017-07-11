from django import forms
from .models import FeedBackMessage


class FeedBackMessageFrom(forms.ModelForm):
    class Meta:
        model = FeedBackMessage
        fields = ('mailer', 'email', 'subject', 'message', )
