from django.shortcuts import render
from crm_client.models import Crm_client
from crm_client.tables import Crm_client_Table
# Create your views here.

def view_table(request):
    table = Crm_client_Table(Crm_client.objects.all())
    return render(request, 'crm_client/base.html', {'table': table})