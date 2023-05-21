from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import StudentVehicle

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
            return render(request, 'confirmation.html') 
    else:
        form = ApplicationForm()
    return render(request, 'form.html', {'form': form})

@login_required       
def vehiclepass(request):
    return render(request,'pass.html')

@login_required
def contact(request):
    return render(request,'contact.html')
