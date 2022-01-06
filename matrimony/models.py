from django.db import models

# Create your models here.
class Customer(models.Model):
    profile = models.CharField(max_length= 20)
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=10,)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    email =  models.EmailField()

    def __str__(self):
        return self.username    

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False


class PersonalInfo(models.Model):
    religion = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20)
    no_of_children = models.CharField(max_length=10)
    child_status = models.CharField(max_length=20)
    religion = models.CharField(max_length=20)
    caste = models.CharField(max_length=20)
    sub_caste = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    username =models.ForeignKey(Customer, null= False, on_delete= models.CASCADE)

class PhysicalAttribute(models.Model):
    height =models.CharField(max_length=20)
    weight =models.CharField(max_length=20)
    body_type =models.CharField(max_length=20)
    complexion =models.CharField(max_length=20)
    physical_status =models.CharField(max_length=20)
    username =models.ForeignKey(Customer, null= False, on_delete= models.CASCADE)

class Education(models.Model):
    highest_qualification =models.CharField(max_length=20)
    additional_degree =models.CharField(max_length=20)
    occupation =models.CharField(max_length=20)
    employedin =models.CharField(max_length=20)
    annual_income =models.CharField(max_length=50)
    username =models.ForeignKey(Customer, null= False, on_delete= models.CASCADE)

class Habit(models.Model):
    diet =models.CharField(max_length=20)
    smoking =models.CharField(max_length=20)
    drinking =models.CharField(max_length=20)
    username =models.ForeignKey(Customer, null= False, on_delete= models.CASCADE)

class Horoscope(models.Model):
    dosh =models.CharField(max_length=20)
    star =models.CharField(max_length=20)
    raasi =models.CharField(max_length=20)
    birth_time =models.TimeField(max_length=20)
    birth_place =models.CharField(max_length=20)
    username =models.ForeignKey(Customer, null= False, on_delete= models.CASCADE)

class Family(models.Model):
    family_status =models.CharField(max_length=20)
    family_type =models.CharField(max_length=20)
    family_value =models.CharField(max_length=20)
    father_occupation =models.CharField(max_length=20)
    mother_occupation =models.CharField(max_length=20)
    brother =models.CharField(max_length=20)
    married_brother =models.CharField(max_length=20)
    sister =models.CharField(max_length=20)
    married_sister =models.CharField(max_length=20)
    username =models.ForeignKey(Customer, null= False, on_delete= models.CASCADE)


class Aboutus(models.Model):
    description =models.CharField(max_length=1000)
    username =models.ForeignKey(Customer, null= False, on_delete= models.CASCADE)






