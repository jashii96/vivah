from django.db import models
from django.contrib.auth.models import User

class PersonalInfo(models.Model):
    mobile = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    marital_status = models.CharField(max_length=50)
    no_ofchild = models.CharField(max_length=50)
    child_status = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    mother_tongue = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    user = models.ForeignKey(User, null= False, on_delete= models.CASCADE)

    