from django.urls import path

from . import views

urlpatterns = [
    path('', views.rentpage, name='rentpage'),
    path("car/<id>",views.rrs, name='rrs'),
  

]