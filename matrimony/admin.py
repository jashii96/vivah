from django.contrib import admin
from django.contrib.auth.models import User
from matrimony.model import Feedback, Profile,PersonalInfo,PhysicalAttribute,Qualification,Habit,Horoscope,FamilyDetails,PhotoAlbum,Kyc
from django.utils.html import format_html
# Register your models here.
'''
class PersonalInfoAdmin(admin.ModelAdmin):
    model = PersonalInfo

class PhysicalAttributeAdmin(admin.ModelAdmin):
    model = PhysicalAttribute

class QualificationAdmin(admin.ModelAdmin):
    model = Qualification

class HabitAdmin(admin.ModelAdmin):
    model = Habit

class HoroscopeAdmin(admin.ModelAdmin):
    model = Horoscope

class FamilyDetailsAdmin(admin.ModelAdmin):
    model = FamilyDetails

class PhotoAlbumAdmin(admin.ModelAdmin):
    model = PhotoAlbum

class KycAdmin(admin.ModelAdmin):
    model = Kyc

class DataAdmin(admin.ModelAdmin):
    inlines = [PersonalInfoAdmin,PhysicalAttributeAdmin,QualificationAdmin,HabitAdmin,HoroscopeAdmin,FamilyDetailsAdmin,PhotoAlbumAdmin,KycAdmin]
'''
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display =['name','email','phone','description']
    list_filter =['email','phone']

class ProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        try:
            return format_html(f'<img src= "{{}}" width=”30" style=”border-radius:50%;”>'.format(object.image.url))
        except:
            pass

admin.site.register(Profile,ProfileAdmin)
admin.site.register(PersonalInfo)
admin.site.register(PhysicalAttribute)
admin.site.register(Qualification)
admin.site.register(Habit)
admin.site.register(Horoscope)
admin.site.register(FamilyDetails)
admin.site.register(PhotoAlbum)
admin.site.register(Kyc)
admin.site.register(Feedback,FeedbackAdmin)



        
