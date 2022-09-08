from django.urls import path
from . import views


app_name = 'internshipcash'
urlpatterns = [
    path('', views.base, name='base'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('transfer', views.transfer, name='transfer'),
    path('transferConfirmed', views.transferConfirmed, name='transferConfirmed'),
]