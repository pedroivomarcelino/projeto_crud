from django.urls import path
from login.views import login, logar

urlpatterns = [
    path('login', login, name='login'),
    path('logar', logar, name='logar'),
]
