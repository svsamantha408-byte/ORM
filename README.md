# Ex02 Django ORM Web Application
## Date: 13.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class car_DB(models.Model ):
    car_name=models.CharField(max_length=18)
    engine_no=models.IntegerField(primary_key="card_ID")
    company=models.CharField(max_length=18)
    fuel_capacity=models.FloatField()
    color=models.CharField(max_length=18)
class car_DBAdmin(admin.ModelAdmin):
    list_display=["car_name","engine_no","company","fuel_capacity","color"]
    admin.py
    from django.contrib import admin
    from .models import (car_DB,car_DBAdmin)
    admin.site.register(car_DB,car_DBAdmin)  
```


## OUTPUT
![alt text](<Screenshot (15).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
