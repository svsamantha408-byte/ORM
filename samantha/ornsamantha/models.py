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