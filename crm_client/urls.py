from django.urls import path

from crm_client.views import clientListView, View_forms

from django.urls import path

urlpatterns = [
    path('client/', clientListView.as_view()),

]