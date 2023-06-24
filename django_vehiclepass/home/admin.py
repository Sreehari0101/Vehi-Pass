from django.contrib import admin
import qrcode
import os
from django.conf import settings
from .models import Booking
from django.urls import reverse

class BookingAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'name', 'admission_number', 'department', 'semester',
    'registration_number', 'user_photo', 'registration_certificate_photo',
    'license_photo', 'insurance_photo', 'owner_declaration_photo', 'is_approved'
)

    list_filter = ('department', 'semester', 'is_approved')
    list_editable = ('is_approved',)

    def save_model(self, request, obj, form, change):
        if obj.is_approved:
            # Generate QR code logic here
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            qr.add_data('192.168.127.140:8000/booking-details/{}/'.format(obj.id))  # for QR code data
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image
            qr_image_path = os.path.join('qr_codes', f'{obj.registration_number}.png')
            qr_image.save(os.path.join(settings.MEDIA_ROOT, qr_image_path))

            # Update the object with the QR code image path
            obj.qr_code = qr_image_path

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        # Delete associated photos and QR code
        obj.registration_certificate_photo.delete()
        obj.license_photo.delete()
        obj.insurance_photo.delete()
        obj.owner_declaration_photo.delete()
        qr_code_path = os.path.join(settings.MEDIA_ROOT, obj.qr_code.name)
        if os.path.exists(qr_code_path):
            os.remove(qr_code_path)

        # Call superclass delete_model method to complete the deletion process
        super().delete_model(request, obj)
admin.site.register(Booking, BookingAdmin)