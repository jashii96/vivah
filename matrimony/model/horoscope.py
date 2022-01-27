from django.db import models
from django.contrib.auth.models import User

class Horoscope(models.Model):
    dosh = models.CharField(max_length= 50, null=True)
    star = models.CharField(max_length= 50, null=True)
    raasi = models.CharField(max_length= 50, null=True)
    birth_time = models.CharField(max_length= 50, null=True)
    birth_place = models.CharField(max_length= 50, null=True)
    kundli = models.ImageField(default = 'sample.jpg' ,upload_to ='horoscope', null = True)
    user = models.ForeignKey(User, null= False, on_delete= models.CASCADE)


    def __str__(self):
        return self.user

