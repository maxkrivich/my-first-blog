from django.conf.urls import url
from .views import CoachDetailView


urlpatterns = [
    url(r'^(?P<pk>\d+)', CoachDetailView.as_view(), name='coach_detail'),
]
