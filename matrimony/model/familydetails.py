from django.db import models
from django.contrib.auth.models import User
class FamilyDetails(models.Model):
    family_status = models.CharField(max_length=50)
    family_type = models.CharField(max_length=50)
    family_value = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=50)
    brothers = models.CharField(max_length=50)
    married_brother = models.CharField(max_length=50)
    sisters = models.CharField(max_length=50)
    married_sister = models.CharField(max_length=50)
    user = models.ForeignKey(User, null= False, on_delete= models.CASCADE)

    