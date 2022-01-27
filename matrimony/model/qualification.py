from django.db import models
from django.contrib.auth.models import User
class Qualification(models.Model):
    highest_education = models.CharField(max_length= 50)
    occupation = models.CharField(max_length= 50)
    employed_in = models.CharField(max_length= 50)
    annual_income = models.CharField(max_length= 50)
    user = models.ForeignKey(User, null= False, on_delete= models.CASCADE)

    def __str__(self):
        return self.user