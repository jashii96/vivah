from django.db import models
from django.contrib.auth.models import User
class Kyc(models.Model):
    adhaar_number = models.CharField(max_length= 20, null=False)
    adhaar_front = models.ImageField(default = 'front.jpg', upload_to = 'kyc', null = True)
    adhaar_back = models.ImageField(default = 'back.jpg', upload_to = 'kyc',null=True)
    user = models.ForeignKey(User, null= False, on_delete= models.CASCADE)

    def __str__(self):
        return self.adhaar_number