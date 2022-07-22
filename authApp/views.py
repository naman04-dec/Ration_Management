from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'authApp/home.html')
#add @login_required and Navbar Items going to check login authentication before displaying any page
@login_required
def gov_view(request):
    return render(request,'authApp/gov.html')

@login_required
def shop_view(request):
    return render(request,'authApp/shop.html')


def cust_view(request):
    return render(request,'authApp/cust.html')


#CustomPage after Logout
def logoutview(request):
    return render(request,'registration/logout.html')

#signup forms
def signupview(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            #But if we use form.save() with User Model form only one isssue thw password data will not be encrypte,so for this we have to face problem during login
            #form.save()
            user=form.save()
            user.set_password(user.password)# Here 'set_password' method take care about Hashing Algo for password
            user.save()
            return HttpResponseRedirect('/accounts/login')#If password data of signUpform not encrypteed then login will not work.


    return render(request,'registration/signup.html',{'form':form})
