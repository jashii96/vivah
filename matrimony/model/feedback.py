from django.db import models



class Feedback(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField(max_length= 50)
    phone = models.IntegerField()
    subject =models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def is_exist(self):
        if Feedback.objects.filter(email = self.email):
            return True

        return False