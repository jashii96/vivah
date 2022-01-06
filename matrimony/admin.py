from django.contrib import admin
from matrimony.models import Customer,PersonalInfo,PhysicalAttribute,Education,Habit,Horoscope,Aboutus,Family
# Register your models here.


class PersonalInfoAdmin(admin.StackedInline):
    model = PersonalInfo

class PhysicalAttributeAdmin(admin.StackedInline):
    model = PhysicalAttribute

class EducationAdmin(admin.StackedInline):
    model = Education

class HabitAdmin(admin.StackedInline):
    model = Habit

class HoroscopeAdmin(admin.StackedInline):
    model = Horoscope


class FamilyAdmin(admin.StackedInline):
    model = Family

class AboutusAdmin(admin.StackedInline):
    model = Aboutus

class PersonalInfoAdmin(admin.StackedInline):
    model = PersonalInfo

class CustomerAdmin(admin.ModelAdmin):
    inlines = [PersonalInfoAdmin,PhysicalAttributeAdmin,EducationAdmin,HabitAdmin,HoroscopeAdmin,FamilyAdmin,AboutusAdmin]



    
admin.site.register(Customer,CustomerAdmin)
admin.site.register(PersonalInfo)
admin.site.register(PhysicalAttribute)
admin.site.register(Education)
admin.site.register(Habit)
admin.site.register(Horoscope)
admin.site.register(Family)
admin.site.register(Aboutus)