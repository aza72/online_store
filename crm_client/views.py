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

        if 'update' in request.POST:
            form = AddRecordClient(request.POST)
            print(form.is_valid())
            if form.is_valid():

                self.update_client(request)
            return HttpResponseRedirect('/client/')

        if request.method == 'POST':
            form = AddRecordClient(request.POST)
            if form.is_valid():
                form.save()
                message = 'Запись добавлена успешно'
                mess(request,message)
                return HttpResponseRedirect('/client/')

            else:
                cut = dict(form.errors)
                for mes in cut:
                    #print(cut[mes][0])
                    message = cut[mes][0]
                    mess(request,message)
                table = Crm_client_Table(Crm_client.objects.all())
                return render(request, 'crm_client/base.html', {'form':form, 'table':table})

        #return HttpResponseRedirect('/client/')
    def delete_client(self,request):
        pks = request.POST.getlist("chek")
        Crm_client.objects.filter(pk__in=pks).delete()
        message = 'Запись удалена успешно'
        mess(request, message)

    def update_client(self,request):
        pks = request.POST.getlist("chek")
        p = Crm_client.objects.get(pk__in=pks)
        print('name')
        name = request.POST.get('name')
        surname = request.POST.getlist("surname")
        patronymic = request.POST.getlist("patronymic")
        car = request.POST.getlist("car")
        telephone = request.POST.getlist("telephone")
        vin = request.POST.getlist("vin")

        if name:
            p.name = name
        p.save()
        print(name)


def mess(request,message):
    messages.success(request, message)






