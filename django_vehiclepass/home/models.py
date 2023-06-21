from django.db import models
from django.contrib.auth.models import User
import qrcode
import os
from django.conf import settings
from django.urls import reverse


# Create your models here
class Booking(models.Model):
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=20,unique=True)
    user_photo = models.ImageField(upload_to='photos', blank=True, null=True)
    registration_certificate_photo = models.ImageField(upload_to='photos')
    license_photo = models.ImageField(upload_to='photos')
    insurance_photo = models.ImageField(upload_to='photos')
    owner_declaration_photo = models.ImageField(upload_to='photos')
    is_approved = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    
    