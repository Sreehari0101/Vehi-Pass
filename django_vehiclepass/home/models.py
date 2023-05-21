from django.db import models
from django.contrib.auth.models import User

# Create your models here
class StudentVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=20)
    registration_certificate_photo = models.ImageField(upload_to='photos/')
    license_photo = models.ImageField(upload_to='photos/')
    insurance_photo = models.ImageField(upload_to='photos/')
    owner_declaration_photo = models.ImageField(upload_to='photos/')
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username