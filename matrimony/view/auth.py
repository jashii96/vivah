from django import views
from django.shortcuts import redirect, render
from django.http import HttpResponse
from matrimony.forms import Registrationform, Loginform
from django.views import View
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
## Class based signup view


class signupview(View):
    def get(self,request):
        form = Registrationform()
        return render(request, template_name= "matrimony/signup.html", context={'form' : form })

    def post(self, request):
        form = Registrationform(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('signup2')

        return render(request, template_name= "matrimony/signup.html", context={'form' : form })


## Basic signupcode
'''
def signup(request):
    if request.method == 'GET':    
        form = Registrationform()
        return render(request, template_name= "matrimony/signup.html", context={'form' : form })
    

    form = Registrationform(request.POST)
    if form.is_valid():
        user = form.save()
        if user is not None:
            return redirect('login')

    return render(request, template_name= "matrimony/signup.html", context={'form' : form })

## basic login code

def login(request):
    return render(request,"matrimony/login.html")

'''

class loginview(View):
    def get(self, request):
        form = Loginform()
        context = {
            'form': form
        }
        return render(request,"matrimony/login.html", context = context)

    def post(self, request):
        form = Loginform(request = request, data = request.POST)
        context = {
            'form': form
        }
        
        if form.is_valid():
            return redirect('myprofile')
        
        return render(request,"matrimony/login.html", context = context)


## Logout Coding

def signout(request):
    logout(request)
    return redirect('home')


def signup2(request):
    return render(request,"matrimony/profile_2.html")



