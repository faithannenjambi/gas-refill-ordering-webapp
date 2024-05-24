from django.contrib import admin
from django.urls import path,include
from .views import home,about,order, order_successful, message

urlpatterns = [
    path('',home,name="home"),
    path('contact/',about,name='about'),
    path('order/',order,name='order'),
    path('order-successful', order_successful, name='order-successful'),
    path('message', message,name='message')
]
