from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^profile/$', core_views.profile, name='profile'),
    url(r'^profile/password/$', core_views.password, name='password'),
    url(r'^admin/', admin.site.urls),
]
