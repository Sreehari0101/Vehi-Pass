from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Booking
from django.contrib import messages
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect



# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def formapply(request):
    if request.method == "POST":
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)  
            booking.is_approved = False  # Set is_approved to False initially
            booking.save()  # Save the form instance

            # Add QR code generation logic here after saving the form

            return redirect('confirmation')  # Redirect to the confirmation page after successful form submission
    else:
        form = BookingForm()

    dict_form = {
        'form': form
    }
    return render(request, 'form.html', dict_form)

@login_required
def vehiclepass(request):
    if request.method == "POST":
        registration_number = request.POST.get('registration_number')
        try:
            booking = Booking.objects.get(registration_number=registration_number)
            if booking.qr_code:
                qr_code_url = request.build_absolute_uri(booking.qr_code.url)
                context = {
                    'booking': booking,
                    'qr_code_url': qr_code_url,
                }
                return render(request, 'pass.html', context)
            else:
                return redirect('vehiclepass')  # Redirect back to the pass page
        except Booking.DoesNotExist:
           return redirect('vehiclepass')  # Redirect back to the pass page
    return render(request, 'pass.html')

@login_required
def contact(request):
    return render(request,'contact.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def booking_details(request, booking_id):
    base_url = 'http://192.168.1.6:8000'
    booking = get_object_or_404(Booking, id=booking_id)
    booking_url = base_url + reverse('booking_details', args=[booking_id])
    return render(request, 'booking_details.html', {'booking': booking, 'booking_url': booking_url})