from django.shortcuts import render
from shopApp import forms,models
from custApp.models import custRation
from custApp import models as mo
from govApp.models import govRation
import datetime
from django.http import HttpResponse


# Create your views here.
def welcomeViewshop(request,form):
    return render(request,'shopApp/govRationForm.html',{'form':forms})


def shopRationForm1(request):
    sugar,wheat,rice=0,0,0
    form=forms.shopRationForm1()
    if request.method=='POST':
        form=forms.shopRationForm1(request.POST)

    if request.method=='POST':
        current_user = request.user
        print(current_user)
        cust=""
        form=forms.shopRationForm1(request.POST)#create new form object with coming data
        date=""

        if form.is_valid():

            aadhar_num=form.cleaned_data['aadhar_num']
            sugar_quant=form.cleaned_data['sugar_quant']
            wheat_quant=form.cleaned_data['wheat_quant']
            rice_quant=form.cleaned_data['rice_quant']
            cust=form.cleaned_data['customer_name']

            #print('Form validation success and printing feedback info')
            #print('Customer Name',form.cleaned_data['customer_name'])#all our form data we get from prdefined dict var-cleaned_data==>{'name':form value}
            #print('Aadhar Num',form.cleaned_data['aadhar_num'])
            #print('Sugar Quantity',form.cleaned_data['sugar_quant'])
            #print('Wheat Quantity',form.cleaned_data['wheat_quant'])
            #print('Rice Quantity',form.cleaned_data['rice_quant'])
            #print('Date',form.cleaned_data['date'])

            gov = govRation.objects.get(shop_name=current_user)


            aadharnum=int(gov.aadhar_num)
            sugarquant=int(gov.sugar_quant)
            wheatquant=int(gov.wheat_quant)
            ricequant=int(gov.rice_quant)



            print("govdata",aadharnum,sugarquant,wheatquant,ricequant)
            if sugarquant>0:
                sugar=sugarquant-sugar_quant
                print(sugar)
                gov.sugar_quant=sugar
                if  wheatquant>0 :
                    wheat=wheatquant-wheat_quant
                    print(wheat)
                    gov.wheat_quant=wheat
                    if  ricequant>0:
                        rice=ricequant-rice_quant
                        print(rice)
                        gov.rice_quant=rice
                        gov.save()

                        datet=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                        #print(datet)

                        if sugarquant>0 and wheatquant>0 and ricequant>0 :
                            cust=mo.custRation(customer_name=cust,aadhar_num=aadhar_num,sugar_quant=sugar_quant,wheat_quant=wheat_quant,rice_quant=rice_quant,date=datet)
                            cust.save()
                            print("cust-save")

            else:
                print("Shop is not having sufficient Quantity")
                quant_alert(request)







            #cust update
            if sugarquant>0 and wheatquant>0 and ricequant>0 :
                datet=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                ob=models.shopRation(customer_name=form.cleaned_data['customer_name'],aadhar_num=form.cleaned_data['aadhar_num'],sugar_quant=form.cleaned_data['sugar_quant'],wheat_quant=form.cleaned_data['wheat_quant'],rice_quant=form.cleaned_data['rice_quant'],date=datet)
                ob.save()
                print("Shop Data Inserted Successfully")
            else:
                print("Shop is not having sufficient Quantity")
                return quant_alert(request)


        return welcomeview(request,form)
    return render(request,'shopApp/govrationform.html',{'form':form})

def welcomeview(request,form):
    return render(request,'shopApp/thanks.html')

def quant_alert(request):
    s="<h1>Not Sufficient Quntity For Distribution</h1>"
    return HttpResponse(s)

    #return render(request,'shopApp/thanks.html',context={'msg':s})
