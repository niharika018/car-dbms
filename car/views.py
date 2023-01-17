from django.shortcuts import render, redirect ,get_object_or_404
from car.models import SALESMAN,CUSTOMER,LOCATION,ORDER,SERVICE
from .forms import ORDER,SERVICE,CUSTOMER
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView 


def customer(request):
    context={}

    form = CUSTOMER(request.POST)

    if form.is_valid():
        form.save()
        return redirect('customerd')

    context['form'] = form
    return render(request,"customer.html",context) 

def order(request):
    context={}

    form = ORDER(request.POST)

    if form.is_valid():
        form.save()
        return redirect('orderd')

    context['form'] = form
    return render(request,"order.html",context) 

def service(request):
    context={}

    form = SERVICE(request.POST)

    if form.is_valid():
        form.save()
        return redirect('serviced')

    context['form'] = form
    return render(request,"service.html",context) 

def search(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = LOCATION.objects.filter(
                Q(location_Id__contains=query_name) | Q(country__contains=query_name)
                )
            return render(request, 'search_results.html', {"results":results})

    return render(request, 'search_results.html')




