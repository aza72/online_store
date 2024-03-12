from django import template

from crm_client.forms import AddRecordClient, AutoClient

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
def modal_window_add():
    form = AddRecordClient()
    form_auto = AutoClient()
    return {'form':form, 'form_auto':form_auto}


