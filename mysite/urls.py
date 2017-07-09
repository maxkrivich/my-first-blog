from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as v1
from . import views as v2
from courses import views as v3
from students import views as v4

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^accounts/login/$', v1.login, name='login'),
    url(r'^accounts/logout/$', v1.logout,
        name='logout', kwargs={'next_page': '/'}),
    url(r'^$', v2.get_home_page, name='home'),
    url(r'^contact/', v2.get_contact, name='contact'),
]
