import re
from . models import *
from django.forms import ModelForm
    
from datetime import datetime

from django.utils import timezone


class EmpForm(ModelForm):
    class Meta:
        model = Emp
        fields = ('name','email','pur_date')


    # def clean_pur_date(self):
    #     valname = self.cleaned_data['pur_date']
    #     data = datetime.strftime(valname,"%Y %B  %d")
    #     return data
    













    # class ProductForm(forms.ModelForm):
    # class Meta:
    #     model = Product
    #     fields = ('image',)

    # def clean_image(self):
    #     image = self.cleaned_data.get('image', False)
    #     if image:
    #         # validate image
    #     return None
      