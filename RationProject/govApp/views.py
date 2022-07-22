from django.shortcuts import render
from govApp import forms,models

# Create your views here.
def welcomeView(request,form):
    return render(request,'govApp/govRationForm.html',{'form':forms})

def govRationForm1(request):
    form=forms.govRationForm2()
    if request.method=='POST':
        form=forms.govRationForm2(request.POST)

    #Save Model form data into databases
    if request.method=='POST':
        form=forms.govRationForm2(request.POST)#create new form object with coming data
        if form.is_valid():
            print('Form validation success and printing feedback info')
            print('Shop Name',form.cleaned_data['shop_name'])#all our form data we get from prdefined dict var-cleaned_data==>{'name':form value}
            print('Aadhar Num',form.cleaned_data['aadhar_num'])
            print('Suqgar Quantity',form.cleaned_data['sugar_quant'])
            print('date',form.cleaned_data['date'])

            ob=models.govRation(shop_name=form.cleaned_data['shop_name'],aadhar_num=form.cleaned_data['aadhar_num'],sugar_quant=form.cleaned_data['sugar_quant'],wheat_quant=form.cleaned_data['sugar_quant'],rice_quant=form.cleaned_data['sugar_quant'],date=form.cleaned_data['date'])
            ob.save()
            print("Data Inserted Successfully")

        return welcomeview(request)
    return render(request,'govApp/govrationform.html',{'form':form})

def welcomeview(request):
    return render(request,'govApp/thanks.html')
