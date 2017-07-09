from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.student_list, name='student_list'),
    url(r'^(?P<pk>\d+)/delete/$', views.student_delete, name='student_delete'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.student_edit, name='student_edit'),
    url(r'^(?P<pk>\d+)', views.student_detail, name='student_detail'),
    url(r'^new/$', views.student_new, name='student_new'),
]
