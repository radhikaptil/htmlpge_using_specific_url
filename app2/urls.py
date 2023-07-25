from django.urls import path
from app2.views import *

ap_name='some'

urlpatterns=[
    path('find/',find,name='find'),
    path('temp/',temp,name='temp'),
]