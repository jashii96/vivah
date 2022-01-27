from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from matrimony.model import Profile
from PIL import Image

class Registrationform(UserCreationForm):
    first_name = forms.CharField(max_length = 20, required = True)
    last_name = forms.CharField(max_length = 20, required = True)
    email = forms.EmailField(max_length = 30, required = True)
    
    class Meta:
        model = User

        fields =("first_name","last_name" ,"username", "email","password1","password2")
        #fields = ["First_Name", "Last_Name", "Eamil", "Password1", "password2"]

    def clean_email(self):
        email =  self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email = email)
        except:
            return email

        if user is not None:
            raise ValidationError("User Already Exist")



# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')

# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)