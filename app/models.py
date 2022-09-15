from datetime import datetime
import email
from django.db import models
from datetime import datetime,date
# Create your models here.

class Emp(models.Model):
    name = models.CharField( max_length=50)
    email= models.EmailField()
    pur_date = models.DateTimeField("Enroll Date (yyyy/mm/dd)" ,auto_now=False,auto_now_add=False)
    exp_date = models.DateTimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    


    def __str__(self):
        return self.name







#https://stackoverflow.com/questions/12806771/django-modelform-validation

