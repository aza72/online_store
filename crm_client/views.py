import json

from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from crm_client.forms import *
from crm_client.forms import AddRecordClient
from crm_client.models import Crm_client, BrandAuto
from crm_client.tables import Crm_client_Table
# Create your views here.
from django_tables2 import SingleTableView, LazyPaginator, SingleTableMixin, RequestConfig
from django.views.generic.edit import FormView, DeleteView

from crm_client.templatetags.common_tags import modal_window_add
from crm_client.utils import get_records, check_brand


class clientListView(SingleTableView):
    # form = AddRecordClient()
    model = Crm_client
    table_class = Crm_client_Table
    template_name = 'crm_client/crm.html'
    choice = BrandAuto.objects.all()
    # extra_context = {'form': form}

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

class client_baseListView( SingleTableView):
    form = AddRecordClient()
    model = Crm_client
    #paginate_by = 5
    table_pagination = {'per_page': 5, 'page': 1}
    table_class = Crm_client_Table
    template_name = 'crm_client/client_base.html'
    choice = BrandAuto.objects.all()
    extra_context = {'form': form}
#123123
    def post(self,request):
        #pks = request.POST
        form = AddRecordClient(request.POST)
        message = request.POST
        print(message)

        print()
        if form.is_valid():
            print('125')
            #form.save()
        else:
            print(form.errors.values())

        table = Crm_client_Table(Crm_client.objects.all())
        table.paginate(page=request.POST.get("page", 1),per_page=5)
        #return HttpResponse({'table': table})
        #RequestConfig(request, paginate={"per_page": 5}).configure(table)
        return render(request, 'crm_client/client_base.html',{'table': table})

# def validate_username(request):
#     print("123")


class DeleteClientView(DeleteView):  # Создание нового класса
    pk_url_kwarg = 'pk'
    model = Crm_client
    # context_object_name = 'pk'
    # template_name = 'crm_client/client_base.html'
    success_url = reverse_lazy('/client-base')

    # def __init__(self, *args, **kwargs):
    #     print("constructor")
    #     print(type(kwargs.items()))
    #     self.kwargs =kwargs

    def get_object(self, queryset=None):
        print("123")
        print(self.kwargs)
        print("321")
        return Crm_client.objects.filter(pk=4)


def custom_middleware(request,**kwargs):
    data = request.POST.get("pk")
    print(request)
    obj = Crm_client.objects.filter(pk=data)

    pk_url_kwarg = {

        'pk': 3,
        "method":'POST'
    }
    answer = DeleteClientView.as_view()(request)
    # answer.delete(request,**pk_url_kwarg )
    # answer.get_object=data
    print(answer)
    return answer





class BaseClientView(ListView):
    model = Crm_client
    template_name = 'crm_client/client_base.html'
    message = None    #Сообщения в таблицу
    form = AddRecordClient()
    formset = ModelAutoForm()
    # errors = None   #Ошибки валидации формы добавления

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['formset'] = self.formset
        if self.message is not None:
            context['message'] = self.message
        # if self.errors is not None:
        #     context['errors'] = self.errors
        return context
    def post(self,request,*args,**kwargs): #Прием ajax запроса
        self.object_list = self.get_queryset()
        # self.message = self.message
        if (request.POST.get("method")=="delete"): #если нажата кнопка delete
            query_delete = get_records(request)
            query_delete.delete()
            self.message = 'Записи успешно удалены'

        elif(request.POST.get("method")=="add"): #если нажата кнопка add
            form = AddRecordClient(request.POST)

            if form.is_valid():
                form.save()
                self.form = AddRecordClient()
                self.message = 'Записи успешно добавлены'

            else:
                self.form = form

        elif (request.POST.get("method") == "add_auto"):  # если нажата кнопка add_auto
            BrandFormset = inlineformset_factory(BrandAuto,ModelAuto)
            # self.formset = BrandFormset()






            # req = check_brand(request)
            # request.POST = req
            # form = AutoClient(request.POST)
            # print(form)
            # form['brand'] = req

            # if form.is_valid():
            #     self.form = AutoClient()
            #     self.message = 'Автомобиль успешно добавлен'
            #
            # else:
            #     self.form = form

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
            



    # def get_queryset(self):
    #     object_list = Crm_client.objects.all()
    #     return object_list