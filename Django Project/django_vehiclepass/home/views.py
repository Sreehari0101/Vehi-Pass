from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def form(request):
    return render(request,'form.html')
def vehiclepass(request):
    return render(request,'pass.html')
def contact(request):
    return render(request,'contact.html')
