from django.contrib import admin
from django.conf.urls import url, include
from registration import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^registration$', views.registration, name='registration')
]
