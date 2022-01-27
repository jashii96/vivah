from django.db import models
from django.contrib.auth.models import User
class PhysicalAttribute(models.Model):
    height = models.CharField(max_length= 50)
    weight = models.CharField(max_length= 50)
    body_type = models.CharField(max_length= 50)
    complexion = models.CharField(max_length= 50)
    physical_status = models.CharField(max_length= 50)
    user = models.ForeignKey(User, null= False, on_delete= models.CASCADE)


    def __str__(self):
        return self.user