from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('', HomePage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('adduser/', AddUser.as_view(), name='add_user'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('info/<slug:info_slug>/', ShowUserInfo.as_view(), name='info'),
    path('door/<slug:door_slug>/', UserDoorShow.as_view(), name='door'),

]
