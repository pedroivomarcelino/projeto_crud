from django.urls import path
from login.views import login, logar, logout

urlpatterns = [
    path('login', login, name='login'),
    path('logar', logar, name='logar'),
    path('logout', logout, name='logout'),
]
