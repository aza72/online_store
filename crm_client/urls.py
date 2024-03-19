from django.urls import path

from crm_client.views import *

from django.urls import path

urlpatterns = [
    path('client/', clientListView.as_view(), name='client'),
    path('test/', test_list, name='test'),
    path('client-base/',  client_baseListView.as_view(), name='client-base'),
    # path('validate_username', validate_username, name='validate_username')
]