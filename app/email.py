
from email import message
from . models import *

from django.core.mail import send_mail
from django.conf  import settings

def sen_reg_email(email):
    subject = "Purchase"
    message = "Purchase Sucessfully , Please visit again "
    email_from = settings.EMAIL_HOST
    send_mail(subject,message, email_from,[email])
    print("Message Sent")
   




# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )














# from email import message
# from django.core.mail import send_mail
# import random
# from . models import *

# from django.conf  import settings

# def send_otp_email(email):
#     subject = 'Your account Varification mail'
#     otp = random.randint(1000,20000)
#     message = f'your Otp is {otp}'  
#     email_from = settings.EMAIL_HOST
#     send_mail(subject, message, email_from, [email])

#     user_obj = User.objects.get(email=email)
#     user_obj.otp = otp
#     user_obj.save()

