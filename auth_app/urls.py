from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page, name= "login_page"),
    path('signup/',signup_page,name= "signup_page"),
    path('logout/',logout_page,name= "logout"),
]

