from django.conf.urls import url
from . import views

from .views import StudentDetailView, StudentDeleteView, StudentUpdateView
from .views import StudentCreateView, StudentListView

urlpatterns = [
    url(r'^$', StudentListView.as_view(), name='student_list'),
    url(r'^(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='student_delete'),
    url(r'^(?P<pk>[0-9]+)/edit/$',
        StudentUpdateView.as_view(), name='student_edit'),
    url(r'^(?P<pk>\d+)', StudentDetailView.as_view(), name='student_detail'),
    url(r'^new/$', StudentCreateView.as_view(), name='student_new'),
]
