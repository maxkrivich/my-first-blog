from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new/$', views.course_new, name='course_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.course_edit, name='course_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.course_delete, name='course_delete'),
    url(r'^(?P<pk>\d+)/lesson/$', views.add_lesson_to_course,
        name='add_lesson_to_course'),
    url(r'^lesson/(?P<pk>\d+)/delete/$', views.lesson_delete, name='lesson_delete'),
    url(r'^lesson/(?P<pk>\d+)/edit/$', views.lesson_edit, name='lesson_edit'),
    url(r'^(?P<pk>\d+)', views.course_detail, name='course_detail'),
]
