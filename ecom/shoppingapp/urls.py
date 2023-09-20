from django.contrib import admin
from django.urls import path,include

from shoppingapp import views
app_name='shoppingapp'
urlpatterns = [
    path('',views.allProductCategary,name='allproduct'),
    path('<slug:c_slug>/',views.allProductCategary,name="product_by_categary"),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name="productdetail")
]