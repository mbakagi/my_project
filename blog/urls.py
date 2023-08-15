from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.index , name="index"),
    path('specific/', views.specific , name="specific"),
    path('getresp/', views.getresponse,name="getresponse")


]
