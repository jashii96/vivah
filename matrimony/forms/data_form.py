from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from matrimony.model import Profile


class Dataform(UserCreationForm):
    Date_of_Birth = forms.DateField(required = True)
    Marital_Status = forms.CharField(max_length = 30, required = True)
    Religion = forms.CharField(max_length = 30, required = True)
    Caste = forms.CharField(max_length = 30, required = True)
    Mother_Tongue = forms.CharField(max_length = 30, required = True)
    City = forms.CharField(max_length = 30, required = True)
    State = forms.CharField(max_length = 30, required = True)
    Country = forms.CharField(max_length = 30, required = True)

    class Meta:
        model = User

        fields =("Date_of_Birth","Marital_Status","Religion" ,"Caste","Mother_Tongue","City","State","Country")
        #fields = ["First_Name", "Last_Name", "Eamil", "Password1", "password2"]
