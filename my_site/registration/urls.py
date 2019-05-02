from django.contrib import admin
from django.conf.urls import url, include
from registration import views

urlpatterns = [
    url(r'^registration/', views.landing, name='registration')
]
