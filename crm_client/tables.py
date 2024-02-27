import django_tables2 as tables
from .models import Crm_client




class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class Crm_client_Table(tables.Table):
    id = tables.Column(accessor='id')
    chek = CheckBoxColumnWithName(verbose_name="Выбор", accessor='pk')
    name = tables.Column(verbose_name='Имя')
    surname = tables.Column( verbose_name='Фамилия')
    patronymic = tables.Column( verbose_name='Отчество')
    car = tables.Column( verbose_name='Автомобиль')
    telephone = tables.Column( verbose_name='Телефон')
    vin = tables.Column( verbose_name='VIN-номер')
    ord = tables.Column(default='Нет информации', verbose_name='Заказы')
    bonuses = tables.Column(default='Нет информации', verbose_name='Бонусы')
    data_create = tables.Column( default='Нет информации',verbose_name='Время создания')

    class Meta:
        attrs = {"class": "table  table-bordered border-dark  table-secondary table-striped table-hover ", "tr": "table-danger"}
        model = Crm_client
        template_name = 'django_tables2/bootstrap5.html'
        sequence = ("id", "chek", "name", "surname", "patronymic", "car",
                    "telephone", "vin", "ord", "bonuses", "data_create")

