from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^logout/', views.signout, name='signout'),
    url(r'^auth_error/', views.auth_error, name='auth_error'),
)
