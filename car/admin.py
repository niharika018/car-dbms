from django.contrib import admin

# Register your models here.
from .models import SALESMAN,CUSTOMER,LOCATION,ORDER,SERVICE

admin.site .register(SALESMAN)

admin.site .register(CUSTOMER)

admin.site .register(LOCATION)

admin.site .register(ORDER)

admin.site .register(SERVICE)