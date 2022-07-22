"""AuthProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from authApp import views
from govApp import views as gov_views

urlpatterns = [
    #authApp urls
    path('admin/', admin.site.urls),
    path('',views.home_view),
    path('gov/',views.gov_view),
    path('shop/',views.shop_view),
    path('cust/',views.cust_view),
    #Add auth url urlpatterns
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logoutview),
    path('signup/',views.signupview),

    #shopapp-URLs
    path('govForm/',gov_views.govRationForm1),

]
