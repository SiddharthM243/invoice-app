from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=250)
    date = models.DateField()
    
class Items(models.Model):
    invoices = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items", blank = True, null = True)
    desc = models.TextField()
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
