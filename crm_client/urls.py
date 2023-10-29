from django.urls import path

from crm_client.views import clientListView

from django.urls import path

urlpatterns = [
    path('client/', clientListView.as_view(), name='client'),

]