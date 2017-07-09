from django.contrib import admin
from .models import FeedBackMessage


class FeedBackMessageAdmin(admin.ModelAdmin):
    model = FeedBackMessage


admin.site.register(FeedBackMessage, FeedBackMessageAdmin)
