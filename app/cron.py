
from datetime  import datetime

from . models import *
from django.core.mail import send_mail
from django.conf  import settings






def retire_mail():
    today_date = datetime.today()
    date_format = today_date.strftime('%Y-%m-%d')
    print(type(date_format))
    dead_line = Emp.objects.filter(exp_date = date_format)

    if date_format  == dead_line:
        def deadlin_emai(email):
            subject = "Purchase"
            message = "Purchase Sucessfully , Please visit again "
            email_from = settings.EMAIL_HOST
            send_mail(subject,message, email_from,[email])
            print("Message Sent")
            return  deadlin_emai
    else:
        pass
    
retire_mail()
   
