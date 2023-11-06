from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from crm_client.forms import *
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

    # def delete_client(self,request):
    #     print('delete')

    def post(self,request):
        if 'delete' in request.POST:
           self.delete_client(request)
           return HttpResponseRedirect('/client/')

        if request.method == 'POST':
            form = AddRecordClient(request.POST)
            if form.is_valid():
                self.add_client(request)
                form.save()
                message = 'Запись добавлена успешно'
                mess(request,message)

            else:
                return HttpResponse("Invalid data")
                message = 'Ошибка, запись не добавлена!'
                mess(request,message)
                return render(request, 'crm_client/base.html', {'form':form})

        return HttpResponseRedirect('/client/')
    def delete_client(self,request):
        pks = request.POST.getlist("chek")
        p = request.POST.getlist("name", "surname")
        #print(pks)
        #print(p)

        Crm_client.objects.filter(pk__in=pks).delete()
        message = 'Запись удалена успешно'
        mess(request, message)

    def add_client(self, request):
        name = request.POST.getlist("name")
        surname = request.POST.getlist("surname")

        if name:
            message = 'Поле name обязательно для заполнения'
            mess(request,message)


def mess(request,message):
    messages.success(request, message)

def save_client():
    print('delete')

# class CreateCRMClientView(FormView):
#     template_name = 'crm_client/base.html'
#     form_class = AddRecordClient
#     success_url = reverse_lazy('/')



