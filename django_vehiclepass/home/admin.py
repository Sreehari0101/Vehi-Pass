from django.contrib import admin
from .models import StudentVehicle
import qrcode
import os
from django.conf import settings

class FormAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'name', 'admission_number', 'department', 'semester', 'registration_number',
                    'registration_certificate_photo', 'license_photo', 'insurance_photo', 'owner_declaration_photo',
                    'is_approved')
    list_editable = ('is_approved',)


    def save_model(self, request, obj, form, change):
        # Override save_model method to generate QR code only after approval
        if obj.is_approved:
            # Generate QR code logic here
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(obj.id)  # You can customize the data to be encoded in the QR code
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image
            qr_image_path = os.path.join('qr_codes', f'{obj.id}.png')
            qr_image.save(os.path.join(settings.MEDIA_ROOT, qr_image_path))


            # Update the object with the QR code image path
            obj.qr_code = qr_image_path

        super().save_model(request, obj, form, change)


admin.site.register(StudentVehicle, FormAdmin)
