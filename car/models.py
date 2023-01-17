from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class SALESMAN(models.Model) :
    salesman_id  = models.CharField(max_length=10,primary_key = True) 
    salesman_Name = models.CharField(max_length = 100)
    phone_No = models.BigIntegerField()
    email = models.EmailField(max_length = 150)
    salesman_Address = models.TextField()
    commission = models.CharField(max_length=5)

    def __str__(self) :
        a = self.salesman_Name+'-'+self.salesman_id
        return a

class CUSTOMER(models.Model) :
    customer_Id = models.CharField(max_length=10,primary_key = True)
    customer_Name = models.CharField(max_length = 100)
    phone_No = models.BigIntegerField()
    email = models.EmailField()
    customer_address = models.TextField()
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self) :
        a = self.customer_Name
        return a

class LOCATION(models.Model) :
    location_Id = models.CharField(max_length = 10,primary_key = True)    
    country = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    area = models.CharField(max_length = 20)
    pincode = models.BigIntegerField()

    def __str__(self) :
        a = self.country+'-'+self.location_Id
        return a



class ORDER(models.Model) :
    id = models.AutoField(primary_key=True)
    order_Id = models.ForeignKey(User,on_delete=models.CASCADE) 
    salesman_id = models.ForeignKey(SALESMAN, on_delete=models.CASCADE,null=True)
    customer_Id = models.ForeignKey(CUSTOMER, on_delete=models.CASCADE,null=True)
    location_Id = models.ForeignKey(LOCATION, on_delete=models.CASCADE,null=True)
    vehicle_name = models.CharField(max_length = 100)
    vehicle_type = models.CharField(max_length = 30)
    date = models.DateField()
    cost = models.DecimalField(max_digits = 100000 , decimal_places = 3,null=True)

    def __str__(self) :
        a = str(self.order_Id)+'-'+self.vehicle_name
        return a

    def get_absolute_url(self):
        return reverse('orderd')


class SERVICE (models.Model) :
    service_Id = models.ForeignKey(User,on_delete=models.CASCADE) 
    location_Id = models.ForeignKey(LOCATION, on_delete=models.CASCADE)
    service_date = models.DateField()
    vehicle_number = models.CharField(max_length=12,primary_key=True)
    vehicle_issue = models.CharField(max_length = 100)
    delivery_Date = models.DateField(null=True)
    service_cost = models.FloatField(null=True)

    def __str__(self) :
        a = str(self.service_Id)+':'+self.vehicle_issue
        return a

  
