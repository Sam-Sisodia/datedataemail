from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse

# Create your views here.

from . models import *
from . form import *
from . email import *
from datetime import datetime, timedelta,date

from django.utils import timezone

from . cron import *

def get_empdetails(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email= request.POST.get('email')
            pur_date = request.POST.get("pur_date")
            endate = datetime.strptime(pur_date, '%Y-%m-%d').date() + timedelta(days=1)

            user_info = Emp.objects.create(name=name, email=email, pur_date=pur_date,
                                     exp_date=endate )
            user_info.save()
            #sen_reg_email(email=email)
            print(type(user_info.pur_date))
            print(type(user_info.exp_date)) 
            

            return HttpResponse("<h1>Enroll Sucessfully </h1>'")
        else:
            
            
            return HttpResponseNotFound("<h1>Something</h1>'")
    else:
        form = EmpForm()
        return render(request,"wel.html",{'form':form})



def hh(request):
    retire_mail()
    return render(request, "helo.html")























# from datetime import datetime as dtt

# time_only = dtt.strptime('15:30', "%H:%M") - dtt.strptime("00:00", "%H:%M")




# ndate = datetime.strftime(pur_date,'%d %B %Y') + timedelta(days=1)


# date_str = '10-27-2020'

# dto = datetime.strptime(date_str, '%m-%d-%Y').date()