from django.shortcuts import render
from custApp.models import custRation

from django.views.generic import ListView
from custApp import forms
# Create your views here.
class custRationListView(ListView):
    model=custRation

def CustomerForms(request):

    form=forms.CustAadharform()

    if request.method=='POST':
        form=forms.CustAadharform(request.POST)#create new form object with coming data




        if form.is_valid():
            print('Form validation success and printing feedback info',form.cleaned_data['aadhars_num'])
            aadhars_num=str(form.cleaned_data['aadhars_num'])
            models=custRation.objects.filter(aadhar_num=aadhars_num).values('id','customer_name','aadhar_num','sugar_quant','rice_quant','wheat_quant','date')
            print(str(models))


            #context={'form':models }


            return render(request,'custApp/customer.html',context={'model':models})


    #after submit form(post) request is going to come on same page view because we did not define any action
#get data from form request Postif request.method=='POST':

    return render(request,'custApp/aadhar.html',{'form':form})
