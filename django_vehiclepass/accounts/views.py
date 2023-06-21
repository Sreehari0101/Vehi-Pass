from django.core.mail import message
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def handlelogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/accounts/login/')
    return render(request,'login.html')


def handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")

        # print(uname,email,password,confirmpassword)

        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/accounts/signup')

        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName Is Taken")
                return redirect('/accounts/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/accounts/signup')
        except:
            pass

        # Create a new user with the provided username, email, and password
        myuser=User.objects.create_user(username=uname, email=email, password=password)
        messages.success(request,"Signup Success Please login!")
        return redirect('/accounts/login')

    return render(request,'signup.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/accounts/login')


