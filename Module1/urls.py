from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello1/', hello1, name='hello1'),
    path('', newHomePage, name='newHomePage'),
    path('travelPackage/',travelPackage,name='travelPackage'),
    path('print/',print1,name='print1'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('randomcall/', randomcall, name='randomcall'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('getdate',get_date,name='get_date'),
    path('getregistercall/',getregistercall,name='getregistercall'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('piechartcall/',piechartcall,name='piechartcall'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('carrentcall/',carrentcall,name='carrentcall'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
path('feedbackcall/',feedbackcall,name='feedbackcall'),
    path('feedbackfunction/',feedbackfunction,name='feedbackfunction'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
]