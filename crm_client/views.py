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




def dry(request):

    print('srabotalo')
    f=AddRecordClient(request.POST)
    f.save()




class CreateCRMClientView(FormView):
    template_name = 'crm_client/base.html'
    form_class = AddRecordClient
    #success_url = reverse_lazy('client')


    def save_client(self,form):
        client = Crm_client(name=form.cleaned_data['name'],
                            surname=form.cleaned_data['surname'],
                            patronymic=form.cleaned_data['patronymic'],
                            car=form.cleaned_data['car'],
                            telephone=form.cleaned_data['telephone'],
                            vin=form.cleaned_data['vin'])
        client.save()
        return super().form_valid(form)
# def View_forms(request):
#     form = AddRecordClient()
#     return render(request, "crm_client/base.html")


# def view_table(request):
#     table = Crm_client_Table(Crm_client.objects.all())
#     return render(request, 'crm_client/base.html', {'table': table})