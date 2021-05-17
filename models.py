from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

## Product management ......
class pdt_reg_tbl(models.Model):
    pdtname=models.CharField(max_length=100)
    pdtimage=models.FileField(upload_to="media")
    pdtprice=models.CharField(max_length=100)
    pdttax=models.CharField(max_length=100)
    pdtquality=models.CharField(max_length=100)
    pdtstatus=models.CharField(max_length=100)

# # Supplier Registration .....
class supp_reg_table(models.Model):
    supName=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    payment=models.DecimalField(max_digits=9,decimal_places=2)

## category add
class pdt_category_add(models.Model):
    pdtcatname = models.CharField(max_length=100)
    pdtcatstatus = models.CharField(max_length=100)

## stock add

class stock_management(models.Model):
    pdtid = models.ForeignKey(pdt_reg_tbl,on_delete=models.CASCADE)
    stock = models.CharField(max_length=100)

#adding machines
class machine_add(models.Model):
    machinename = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    machineperformance = models.CharField(max_length=100)
