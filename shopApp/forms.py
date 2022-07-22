from django import forms
from shopApp.models import shopRation
from django.core import validators

class shopRationForm1(forms.Form):
    customer_name=forms.CharField(label='Enter Customer Name')
    aadhar_num=forms.IntegerField(label='Enter Aadhar')
    sugar_quant=forms.IntegerField(label='Sugar Quantity in KG')
    wheat_quant =forms.IntegerField(label='Wheat  Quantity in KG')
    rice_quant=forms.IntegerField(label='Rice  Quantity in KG')
    #date=forms.DateTimeField(label='Date')


    def clean(self):
        cleaned_data=super().clean()
        inputcustomer_name=cleaned_data['customer_name']
        inputaadhar_num=cleaned_data['aadhar_num']
        inputsugar_quant=cleaned_data['sugar_quant']
        inputwheat_quant=cleaned_data['wheat_quant']
        inputrice_quant=cleaned_data['rice_quant']


        print("Custom Validation")
        if len(inputcustomer_name)<2:
            raise forms.ValidationError("Custom The Length of the name filled should>=2")

        if len(str(inputaadhar_num))==10:
            raise forms.ValidationError("Custom The Length of the aadhar_num filled should 10")

        if len(str(inputsugar_quant))<2:
            raise forms.ValidationError("Custom The Length of the sugar_quant should 2-3 digit")

        if len(str(inputwheat_quant))<2:
                raise forms.ValidationError("Custom The Length of the wheat_quant filled should 2-3 digit")

        if len(str(inputrice_quant))<2:
                raise forms.ValidationError("Custom The Length of the inputrice_quan filled should 2-3 digit")
