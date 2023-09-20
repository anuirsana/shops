from django.contrib import admin
from django.urls import path,include

from searchapp import views

app_name='searchapp'
urlpatterns=[
    path('',views.SerchResult,name='SerchResult'),
]