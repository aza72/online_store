from django.shortcuts import render

from crm_client.forms import AddRecordClient
from crm_client.models import Crm_client
from crm_client.tables import Crm_client_Table
# Create your views here.
from django_tables2 import SingleTableView


class clientListView(SingleTableView):
    form = AddRecordClient()
    model = Crm_client
    table_class = Crm_client_Table
    template_name = 'crm_client/base.html'
    extra_context = {'form': form}

def View_forms(request):
    form = AddRecordClient()
    return render(request, "crm_client/base.html", {'form': form})


# def view_table(request):
#     table = Crm_client_Table(Crm_client.objects.all())
#     return render(request, 'crm_client/base.html', {'table': table})