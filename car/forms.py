from django import forms
from .models import ORDER,SERVICE,CUSTOMER

class ORDER(forms.ModelForm):
    class Meta:
        model = ORDER
        exclude = ['salesman_id','customer_Id','cost']

class SERVICE(forms.ModelForm):
    class Meta:
        model = SERVICE
        exclude = ['delivery_Date','service_cost']

class CUSTOMER(forms.ModelForm):
    class Meta:
        model = CUSTOMER
        fields = "__all__"
