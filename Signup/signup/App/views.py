from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import extendeduser
# Create your views here.
def index(request):
    if request.method=="POST":
        first_name=request.POST['first-name']
        last_name=request.POST['last-name']
        email=request.POST['email']
        username=request.POST['email']
        orgaization=request.POST['org-name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already Exsits')
                return redirect('/')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                newextendeduser=extendeduser(organization=orgaization,user=user)
                newextendeduser.save()
                messages.info(request,'User created please login!')
                return HttpResponse('Welcome! User created successfully')
        else:
            messages.info(request,'Password Is not matching')
            return redirect('/')
        
    else:
        return render(request,'signup.html') 