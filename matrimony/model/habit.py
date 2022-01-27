from django.db import models
from django.contrib.auth.models import User
class Habit(models.Model):
    diet = models.CharField(max_length= 50)
    smoking = models.CharField(max_length= 50)
    drinking = models.CharField(max_length= 50)
    user = models.ForeignKey(User, null= False, on_delete= models.CASCADE)

    def __str__(self):
        return self.user