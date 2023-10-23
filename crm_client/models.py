from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Crm_client(models.Model):
    name = models.CharField(verbose_name='Имя')
    surname = models.CharField(verbose_name='Фамилия')
    patronymic = models.CharField(verbose_name='Отчество')
    car = models.CharField(verbose_name='Автомобиль')
    telephone = models.CharField(verbose_name='Телефон')
    vin = models.CharField(verbose_name='VIN-номер')
    ord = models.CharField(verbose_name='Заказы')
    bonuses = models.CharField(verbose_name='Бонусы')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')



class payment (models.Model):
    provider = models.IntegerField(verbose_name='Оплата поставщику')

class orders (models.Model):
    id_client = models.IntegerField(verbose_name='ID Клиента')
    name_ord = models.CharField(verbose_name='Деталь')
    article_number = models.CharField(verbose_name='Артикул')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    date_of_arrival = models.DateTimeField(auto_now_add=True, verbose_name='Дата прихода')
    price = models.IntegerField(verbose_name='Цена')
