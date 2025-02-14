
from django.urls import path

from grn_app import views


urlpatterns = [

   # path('create_order/', views.create_grn, name='create_order'),
    path('grndetails/', views.create_grn_details, name='grndetails'),
    path('invdetails/', views.create_inv_details, name='invdetails'),
    
 
]