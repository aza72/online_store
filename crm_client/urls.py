from django.urls import path

from crm_client.views import clientListView, test_list

from django.urls import path

urlpatterns = [
    path('client/', clientListView.as_view(), name='client'),
    path('test/', test_list, name='test'),
]