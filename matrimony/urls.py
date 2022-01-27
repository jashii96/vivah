from django.contrib import admin
from django.urls import path
from matrimony.view import home, signupview,loginview,signout,membership,success,feedbacks,signup2,dataview,profileinfo
from matrimony.view import kyc,qualification,physical_attribute,photo_album,family_details,horoscope,personal_info,habits
from django.conf import settings
from django.conf.urls.static import static
from matrimony.view.contact import contact
from matrimony.view.myprofile import myprofile
from matrimony.view.search import search
from vivah.settings import MEDIA_ROOT,MEDIA_URL,STATIC_URL



urlpatterns = [
    path('', home, name='home'),
    path('logout/', signout, name='logout'),
    path('signup/', signupview.as_view(), name='signup'),
    path('login/', loginview.as_view(), name='login'),
    path('data/', dataview.as_view(), name='data'),
    path('signup2/', signup2, name='signup2'),
    path('feedback/', feedbacks, name='feedback'),
    path('membership-plans/', membership, name='membership'),
    path('success-story/', success, name='success'),
    path('search/', search, name='search'),
    path('contacts/', contact, name='contact'),
    path('myprofile/', myprofile, name='myprofile'),
    path('profileinfo/', profileinfo, name='profileinfo'),
    path('kyc/', kyc, name='kyc'),
    path('qualification-details/', qualification, name='qualification'),
    path('physical-attribute/', physical_attribute, name='physical_attribute'),
    path('personal-info/', personal_info, name='personalinfo'),
    path('horoscope/', horoscope, name='horoscope'),
    path('family-details/', family_details, name='family_details'),
    path('photo-album/', photo_album, name='photo_album'),
    path('habits/', habits, name='habits'),
]

urlpatterns += static(MEDIA_URL, document_root= MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=settings.STATIC_ROOT)