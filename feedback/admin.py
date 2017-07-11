from django.contrib import admin
from .models import FeedBackMessage


class FeedBackMessageAdmin(admin.ModelAdmin):
    model = FeedBackMessage
    search_fields = ['name', 'email', ]
    list_display = ['date', 'email']


admin.site.register(FeedBackMessage, FeedBackMessageAdmin)
