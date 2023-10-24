import django_tables2 as tables
from .models import Crm_client

class Crm_client_Table(tables.Table):
    name = tables.Column(verbose_name='Имя')
    surname = tables.Column( verbose_name='Фамилия')
    patronymic = tables.Column( verbose_name='Отчество')
    car = tables.Column( verbose_name='Автомобиль')
    telephone = tables.Column( verbose_name='Телефон')
    vin = tables.Column( verbose_name='VIN-номер')
    ord = tables.Column( verbose_name='Заказы')
    bonuses = tables.Column( verbose_name='Бонусы')
    data_create = tables.Column( verbose_name='Время создания')

    class Meta:
        model = Crm_client
        template_name = 'django_tables2/bootstrap.html'