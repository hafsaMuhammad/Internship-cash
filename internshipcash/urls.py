from django.urls import path
from . import views


app_name = 'internshipcash'
urlpatterns = [
    path('', views.base, name='base'),
    path('<int:user_id>/home/', views.home, name='home'),
    path('<int:user_id>/transfer/', views.transfer, name='transfer'),
    path('<int:user_id>/transferConfirmed/', views.transferConfirmed, name='transferConfirmed'),
]