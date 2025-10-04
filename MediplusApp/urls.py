from django.urls import path
from .views import *

urlpatterns = [
    path("home/",view_Home, name="home"),  # url=http:127.0.0.1:800/home/
    path("about/",view_About, name="about"),
    path("doctors/",view_Doctors, name="doctors"),
    path('contact/',view_Contact, name="contact"),
    path('services/',view_Services, name='services'),
    path('ErrorPage/',view_404,name="error"),
    path("appointment/",view_appointment, name="appointment"),
    path('login/',view_login, name="login"),
    path('register/',view_register,name="register"),
    path('logout/',view_logout,name="logout"),
]
