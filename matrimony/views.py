from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect, request
from .models import Customer
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
###################################### Hompe Page #################################################

def index(request):
    return render(request,'index.html')

###################################### Feedback #################################################
def feedback(request):
    return render(request,'feedback.html')


###################################### Search page #################################################

def search(request):
    return render(request,'search.html')

###################################### Success Story Code #################################################
def success_story(request):
    return render(request,'success-story.html')

###################################### Membership plan code #################################################

def membership(request):
    return render(request, 'membershipplans.html')


###################################### contact us #################################################

def contactus(request):
    return render(request, 'contactus.html')






###################################### Forgot Password #################################################

def forgot_password(request):
    return render(request,'forgot-password.html')

###################################### Admin Panel #################################################
#def admin(request):
 #   return render(request, 'admin/index.html')
 

###################################### Login Form Code #################################################

def login(request):

    pass   



################################# Registration form Code ######################################################

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:

        PostData=request.POST
        profile = PostData.get('profile')
        gender = PostData.get('gender')
        username = PostData.get('username')
        first_name = PostData.get('fname')
        last_name = PostData.get('lname')
        dob = PostData.get('dob')
        phone = PostData.get('phone')
        email =PostData.get('email')

        #validation
        value={
            'username' : username,
            'first_name':first_name,
            'last_name':last_name,
            'dob':dob,
            'phone': phone
            
        }
        error_message = None

        res=Customer(profile = profile, 
                    gender = gender, 
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    dob = dob,
                    phone = phone,
                    email = email,
                                
                    )             

        isexists = Customer.isExists()
        if not profile:
            error_message ="Choose option For Profile Creation"
        elif not gender:
            error_message = "Choose Gender"

        elif not username:
            error_message = "Choose Gender"
        elif not first_name:
            error_message ="First Name Required!!!"
        elif not last_name:
            error_message = "Last Name Required!!!"
        elif not dob:
            error_message = "DOB Required!!!"
        
        elif not phone:
            error_message = "Phone Number Required!!!"

        elif not email:
            error_message = "Email Required!!!"
        
        
        elif isexists:
           error_message = 'Email Address Already Exist....'

        
        #save
        if not error_message:
            #Customer.password = make_password(Customer.password)
            
            res.save()
            return redirect('signup2')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data)


############################## Signup2 code ##############################################################

def signup2(request):
    PostData=request.POST
    profile = PostData.get('profile')
    gender = PostData.get('gender')
    username = PostData.get('username')
    first_name = PostData.get('fname')
    last_name = PostData.get('lname')
    dob = PostData.get('dob')
    phone = PostData.get('phone')
    email =PostData.get('email')

        #validation
    value={
                'gender': gender,
                'username' : username,
                'first_name':first_name,
                'last_name':last_name,
                'dob':dob,
                'phone': phone,
                'email' : email
            }        

    data = {
                'values' : value
            }
    return render(request,'signup2.html',data)
