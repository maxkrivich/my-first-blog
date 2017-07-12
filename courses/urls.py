from django.conf.urls import url
from . import views

from .views import CourseDetailView, CourseListView, CourseDeleteView
from .views import CourseCreateView, CourseUpdateView, LessonUpdateView
from .views import LessonDeleteView, LessonCreateView

urlpatterns = [
    url(r'^new/$', CourseCreateView.as_view(), name='course_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', CourseUpdateView.as_view(), name='course_edit'),
    url(r'^(?P<pk>\d+)/delete/$', CourseDeleteView.as_view(), name='course_delete'),
    url(r'^(?P<pk>\d+)/lesson/$', LessonCreateView.as_view(),
        name='add_lesson_to_course'),
    url(r'^lesson/(?P<pk>\d+)/delete/$', LessonDeleteView.as_view(), name='lesson_delete'),
    url(r'^lesson/(?P<pk>\d+)/edit/$', LessonUpdateView.as_view(), name='lesson_edit'),
    url(r'^(?P<pk>\d+)', CourseDetailView.as_view(), name='course_detail'),
    url(r'^$', CourseListView.as_view(), name='course_list'),
]
