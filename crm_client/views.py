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
    template_name = 'crm_client/crm.html'
    choice = BrandAuto.objects.all()
    extra_context = {'form': form}

    # def delete_client(self,request):
    #     print('delete')

    def post(self,request):
        print("321")
        if 'delete' in request.POST:
           self.delete_client(request)
           return HttpResponseRedirect('/client/')

        if 'update' in request.POST:

            form = UpdateClient(request.POST)
            print(form.is_valid())
            if form.is_valid():
                c = self.update_client(request)
                if c:
                    message = 'Записи отредактированы успешно'
                    mess(request, message)
            else:
                cut = dict(form.errors)
                for mes in cut:
                    message = cut[mes][0]
                    mess(request, message)

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
                return render(request, 'crm_client/crm.html', {'form':form, 'table':table})


    def delete_client(self,request):
        pks = request.POST.getlist("chek")
        if not pks:
            message = 'Вы не выбрали запись для удаления'
            mess(request, message)
        if pks:
            Crm_client.objects.filter(pk__in=pks).delete()
            message = 'Запись удалена успешно'
            mess(request, message)

    def update_client(self,request):
        #pks = request.POST.getlist("chek")
        if not request.POST.getlist("chek"):
            message = 'Вы не выбрали записи для редактирования'
            mess(request, message)

        for pks in request.POST.getlist("chek"):

            p = Crm_client.objects.get(id=pks)
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            patronymic = request.POST.get("patronymic")
            car = request.POST.get("car")
            telephone = request.POST.get("telephone")
            vin = request.POST.get("vin")
            #print(car)
            if name:
                p.name = name
            if surname:
                p.surname = surname
            if patronymic:
                p.patronymic = patronymic
            if car:
                p.car = BrandAuto.objects.get(pk=car)
            if telephone:
                p.telephone = telephone
            if vin:
                p.vin = vin
            p.save()
            print(pks)
        if request.POST.getlist("chek"):
            return True


def mess(request,message):
    messages.success(request, message)


def test_list(request):
    return render(request, 'crm_client/base.html', )

class client_baseListView(SingleTableView):
    form = AddRecordClient()
    model = Crm_client
    table_class = Crm_client_Table
    template_name = 'crm_client/client_base.html'
    choice = BrandAuto.objects.all()
    extra_context = {'form': form}

    def post(self,request):
        pks = request.POST.getlist("chek")
        print(pks)
# def validate_username(request):
#     print("123")
