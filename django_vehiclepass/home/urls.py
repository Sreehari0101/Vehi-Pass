from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('form/', views.form,name='formapply'),
    path('pass/', views.vehiclepass,name='qrpass' ),
    path('contact/', views.contact,name='contact'),
]
