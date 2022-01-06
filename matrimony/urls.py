from django.contrib import admin
from django.urls import path
from matrimony.views import index,search,success_story,membership,feedback,contactus,login,signup,forgot_password,signup2

urlpatterns = [
    path('', index, name='home'),
    path('search/', search, name='search'),
    path('success-story/', success_story, name='success'),
    path('membership/', membership, name='membership'),
    path('feedback/',  feedback, name='feedback'),
    path('contactus/', contactus, name='contacts'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', forgot_password, name='fpassword'),
    #path('admin-login/', admin, name='admin_home'),
    path('signup2/', signup2, name='signup2'),

]
