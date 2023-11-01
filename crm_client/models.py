from django.db import models

# Create your models here.
from django.db import models


class Crm_client(models.Model):
    chek = models.BooleanField(default=False, verbose_name='Выбор')
    name = models.CharField(blank=True,max_length=255,verbose_name='Имя')
    surname = models.CharField(blank=True,max_length=255,verbose_name='Фамилия')
    patronymic = models.CharField(blank=True,max_length=255,verbose_name='Отчество')
    car = models.CharField(blank=True,max_length=255,verbose_name='Автомобиль')
    telephone = models.CharField(max_length=255,verbose_name='Телефон')
    vin = models.CharField(blank=True,max_length=255,verbose_name='VIN-номер')
    ord = models.CharField(blank=True,max_length=255,verbose_name='Заказы')
    bonuses = models.CharField(blank=True,max_length=255,verbose_name='Бонусы')
    data_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

class BrandAuto(models.Model):
    auto_brand = models.CharField(blank=True, max_length=255, verbose_name='Марка авто')


    def __str__(self):
        return self.auto_brand


#
#
# class payment (models.Model):
#     provider = models.IntegerField(verbose_name='Оплата поставщику')
#
# class orders (models.Model):
#     id_client = models.IntegerField(verbose_name='ID Клиента')
#     name_ord = models.CharField(verbose_name='Деталь')
#     article_number = models.CharField(verbose_name='Артикул')
#     data_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
#     date_of_arrival = models.DateTimeField(auto_now_add=True, verbose_name='Дата прихода')
#     price = models.IntegerField(verbose_name='Цена')
