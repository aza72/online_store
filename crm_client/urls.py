from django.urls import path

from crm_client.views import view_table




from django.urls import path

urlpatterns = [
    path('client/', view_table),

]