from django.contrib import admin
from django.urls import path
from  app import views

urlpatterns = [
    path('add',views.get_empdetails,name='emp_data'),
    path('',views.hh)

]
