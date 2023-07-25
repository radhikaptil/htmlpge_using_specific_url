from django.urls import path
from app1.views import *

ap_name='anything'

urlpatterns=[
    path('max/',max,name='max'),
    path('min/',min,name='min'),
]