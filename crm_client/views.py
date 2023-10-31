from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from crm_client.forms import AddRecordClient
from crm_client.models import Crm_client
from crm_client.tables import Crm_client_Table
# Create your views here.
from django_tables2 import SingleTableView
from django.views.generic.edit import FormView

class clientListView(SingleTableView):
    form = AddRecordClient()
    model = Crm_client
    table_class = Crm_client_Table
    template_name = 'crm_client/base.html'
    extra_context = {'form': form}
    def post(self,request):
        if request.method == 'POST':
            f = AddRecordClient(request.POST)
            if f.is_valid():
                f.save()
                message = 'Запись добавлена успешно'
                mess(request,message)
        else:
            message = 'Ошибка, запись не добавлена!'
            mess(request,message)

        return HttpResponseRedirect('/client/')
def mess(request,message):
    messages.success(request, message)

def save_client():
    print('delete')

# class CreateCRMClientView(FormView):
#     template_name = 'crm_client/base.html'
#     form_class = AddRecordClient
#     success_url = reverse_lazy('/')



