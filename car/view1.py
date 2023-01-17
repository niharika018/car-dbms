from django.shortcuts import render, redirect ,get_object_or_404
from car.models import SALESMAN,CUSTOMER,LOCATION,ORDER,SERVICE
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView 

