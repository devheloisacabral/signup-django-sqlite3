from django.urls import path
from app_singup import views

urlpatterns = [
    path('',views.home,name='home'),
    path('users/',views.users, name='list')
]
