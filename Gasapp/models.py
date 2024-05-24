from django.db import models

class Order(models.Model):
     cylinder_size = models.IntegerField()
     quantity = models.IntegerField()
     full_name = models.CharField(max_length=100)
     phone_number = models.CharField(max_length=11)
     address = models.TextField(max_length=200)
     total_amount = models.CharField(max_length=20)
    

class Contact(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=50)
     message = models.TextField(max_length=200)