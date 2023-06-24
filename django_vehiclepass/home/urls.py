from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('form/', views.formapply,name='formapply'),
    path('pass/', views.vehiclepass,name='vehiclepass'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('booking-details/<int:booking_id>/', views.booking_details, name='booking_details'),
]
