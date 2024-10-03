from django.urls import path
from .views import *

urlpatterns = [
    path('home/',    home,name='home'),
    path('signup/',  signup,name='signup'),
    path('login/',   signup,name='signup'),
]