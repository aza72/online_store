from django import template
register = template.Library()


@register.inclusion_tag('tmptag/main_menu.html')
def show_main_menu():
    menu_items = ['Клиент','Бонусная система','Заказы','Статистика','Клиентская база',]
    return {"menu_items": menu_items,}