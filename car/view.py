from django.shortcuts import render, redirect,HttpResponseRedirect
from django.db.models import Q 
from car.models import SALESMAN,CUSTOMER,LOCATION,ORDER,SERVICE
from django.views.generic import TemplateView, ListView

def Orderd(request) :
	bb = ORDER.objects.filter(order_Id=request.user)
	if request.method == "POST":
		bb.delete()
		return HttpResponseRedirect("/orderd")
	context = {'od':bb}
	return render(request,"orderd.html",context)

def Serviced(request) :
	bb = SERVICE.objects.filter(service_Id=request.user)
	if request.method == "POST":
		bb.delete()
		return HttpResponseRedirect("/serviced")
	context = {'sd':bb}
	return render(request,"serviced.html",context)


def loc(request) :
	bb = LOCATION.objects.all()
	context = {'loc':bb}
	return render(request,"loc.html",context)

def customerd(request) :
	bb = CUSTOMER.objects.filter(user_name=request.user)
	context = {'cus':bb}
	return render(request,"customerd.html",context)


