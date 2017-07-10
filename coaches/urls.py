from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)', views.coach_detail, name='coach_detail'),
]
