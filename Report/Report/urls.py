"""Report URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name= 'login'),
    path('report_mainpost', views.mainpost),
    path('signup/', views.signup, name = 'signup'),
    path('home/', views.home, name = 'home'),
    path('report_signuppost', views.signuppost),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('newreport/', views.createreport, name = 'create'),
    path('report_postcreatereport/', views.postcreatereport, name='report'),
    path('logout/', views.logout, name='log'),
    path('checkreport/', views.checkreport, name='check'),
    path('report_postcheck/', views.postcheck, name='postcheck'),
    path('lostpassword/', views.lostpassword, name='lostpassword'),
    path('report_admincheck/', views.admincheck, name='admincheck'),
    path('report_postadmincheck/', views.postadmincheck, name='postadmincheck'),
    path('report_admindetail/', views.admindetail, name='admindetail'),
    path('report_lostpassword/', views.lostpassword, name='lostpassword'),

]


urlpatterns += staticfiles_urlpatterns()