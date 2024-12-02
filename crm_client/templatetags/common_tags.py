from django import template

from crm_client.forms import AddRecordClient
from crm_client.models import Crm_client

register = template.Library()


@register.inclusion_tag('tmptag/main_menu.html')
def show_main_menu():
    menu_items = ['Клиент','Бонусная система','Заказы','Статистика','Клиентская база',]
    return {"menu_items": menu_items,}

@register.inclusion_tag('tmptag/header.html')
def show_header_menu():
    header_menu_items = ['Войти','Регистрация',]
    return {"header_menu_items": header_menu_items,}

@register.inclusion_tag('tmptag/modal_window_add.html')
def modal_window_add(errors,form,formset):
    # form = AddRecordClient()
    # form_auto = AutoClient()
    errors = errors
    return {'form':form, 'formset':formset, 'errors':errors}

@register.inclusion_tag('tmptag/table_clients.html')
def show_table_clients():
    client = Crm_client.objects.all()
    return {'client':client}
