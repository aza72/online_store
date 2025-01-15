from django.urls import path

from crm_client.views import *

from django.urls import path

urlpatterns = [
    path('client/', clientListView.as_view(), name='client'),
    path('test/', test_list, name='test'),
    path('client-base/',  Crm_clientListView.as_view(), name='client-base'),
    path('custom-middleware/', custom_middleware, ),

]