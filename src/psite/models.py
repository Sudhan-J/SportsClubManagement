from django.db import models
from django.db.models.base import ModelState

# Create your models here.
class Branch(models.Model):
    # Br_ID = models.IntegerField(primary_key=True)
    Br_name = models.CharField(max_length=30)
    Br_manager = models.CharField(max_length=20)
    Br_location = models.CharField(max_length=30)
    Br_phone = models.BigIntegerField()
    def __str__(self):
        return self.Br_name



class Event(models.Model):
    # EV_ID = models.IntegerField(primary_key=True)
    E_name = models.CharField(max_length=30)
    E_teams = models.CharField(max_length=30,default=None)
    E_date = models.DateField()
    E_time = models.TimeField()
    E_location = models.CharField(max_length=30)
    E_price = models.IntegerField()
    E_seat = models.IntegerField()
    def __str__(self):
        return self.E_name


class Customer(models.Model):
    # Cust_ID = models.IntegerField(primary_key=True)
    C_name = models.CharField(max_length=20)
    C_phone = models.BigIntegerField()
    C_address = models.TextField()
    C_mail = models.EmailField()
    BOOK = models.ManyToManyField(Event)
    C_password = models.CharField(max_length=200)
    def __str__(self):
        return self.C_name


class Employee(models.Model):
    # E_ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Salary = models.IntegerField()
    Br = models.ForeignKey(Branch,on_delete=models.CASCADE)
    MailID = models.EmailField()
    Phone = models.BigIntegerField()
    Department = models.TextField()
    Designation = models.CharField(max_length=30)
    ATTEND = models.ManyToManyField(Event)
    def __str__(self):
        return self.Name

class EventReg(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    # ph_number = models.BigIntegerField()
    details = models.TextField()
    def __str__(self):
        return self.name

class BOOK(models.Model):
    # Ticket_ID = models.IntegerField(primary_key=True)
    T_date = models.DateField()
    No_seats = models.IntegerField(default=None)
    Cust = models.ForeignKey(Customer,on_delete=models.CASCADE)
    EV = models.ForeignKey(Event,on_delete=models.CASCADE)
    def __str__(self):
        return self.EV

class ATTEND(models.Model):
    E = models.ForeignKey(Employee,on_delete=models.CASCADE)
    EV = models.ForeignKey(Event,on_delete=models.CASCADE)
    def __str__(self):
        return self.EV