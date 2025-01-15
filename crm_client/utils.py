from django.db.models import Q

from crm_client.forms import SearchClientForm
from crm_client.models import *


def get_records(request, *args, **kwargs): #Получение записи из бд
    pk = request.POST.getlist('pk[]')
    pk = list(map(int, pk))
    query = Crm_client.objects.filter(pk__in=pk)
    return query

def check_brand(request, *args, **kwargs):
    brand = request.POST.get('brand')
    brand = BrandAuto.objects.get(auto_brand__iexact=brand)
    post = request.POST.copy()
    post['brand'] = 2
    if brand:
        pass
        # request.POST['brand'] = brand.pk
        # print(req)
    return post

def control_match_upper_register(brand, modal, *args, **kwargs):
    brand = brand.upper()
    modal = modal.upper()
    data = {
        'add_auto_brand': brand,
        'add_model': modal
    }
    return  data
#Поиск обьекта в бд
def get_or_none(classmodel, **kwargs):
    try:
        classmodel.objects.get(**kwargs)
        return False
    except classmodel.DoesNotExist:
        return True

#Поиск клиентов
def search_client(search_query):
    form = SearchClientForm(search_query.request.POST)
    if form.is_valid():
        req = form.cleaned_data['search']
        result = Crm_client.objects.filter(
                Q(name__icontains=req) |
                Q(surname__icontains=req) |
                Q(car__auto_brand__icontains=req) |
                Q(telephone__icontains=req)
            )

    else:
        result = Crm_client.objects.all()


    return result