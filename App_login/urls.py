from django.urls import path
from .views import *

urlpatterns = [
    path('',profile,name='profile'),
    path('signup/',sign_up,name='signup'),
    path('login/',log_in,name='login'),
    path('logout/',log_out, name='logout'),
    path('update-profile/',ChangeProfile,name='update-profile'),
    path('update-password/',passChange,name='update-password'),
    
]