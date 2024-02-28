from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    class Meta:
        db_table = "Register"

class form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    phonenumber = models.IntegerField()
    comments = models.CharField(max_length=100)
    class Meta:
        db_table = "form"

