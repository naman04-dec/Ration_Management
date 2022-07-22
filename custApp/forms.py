from django import forms

class CustAadharform(forms.Form):
    aadhars_num=forms.CharField()  #no need to given length here like models. it is optional
