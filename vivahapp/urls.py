from django.urls import path
from django.urls.conf import include
from vivahapp import views

urlpatterns = [
path('',views.profile_list, name='list'),
path('search/',views.profile_search_list, name='search1'),
path('search_id/',views.profile_search_id, name='search2'),
path('create/',views.profile_create, name='create'),
path('myprofile/',views.my_profile, name='myprofile'),
path('all_profiles/',views.profile_list_all, name='allprofiles'),
path('myprofile/edit/',views.myprofile_update, name='myedit'),
path('details/',views.profile_detail, name='detail'),
path('myprofile/update/',views.profile_update, name='edit'),
path('delete/',views.profile_delete),

]