from django import forms
from django.core.exceptions import ValidationError

from crm_client.models import Crm_client, BrandAuto
from crm_client.views import *


# class AddRecordClient(forms.Form):
#
#     name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
#     surname = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
#     patronymic = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
#     car = forms.ModelChoiceField(empty_label='Авто',label=False, queryset=BrandAuto.objects.all())
#     telephone = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
#     vin = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'VIN-номер'}))
#     #ord = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Заказы'}))
#     #bonuses = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Бонусы'}))
#     # data_create = forms.DateTimeField(auto_now_add=True, verbose_name='Время создания')

class AddRecordClient(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name']= forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
        self.fields['surname']=forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
        self.fields['patronymic'] = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
        self.fields['car'] = forms.ModelChoiceField(empty_label='Авто',label=False, required=False, queryset=BrandAuto.objects.all())
        self.fields['telephone'] = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
        self.fields['vin'] =forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'VIN-номер'}))


    # name = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    # surname = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    # patronymic = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    # car = forms.ModelChoiceField(empty_label='Авто',label=False, required=False, queryset=BrandAuto.objects.all())
    # telephone = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    # vin = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'VIN-номер'}))



    class Meta:
        model = Crm_client
        fields = [ 'name', 'surname', 'patronymic', 'car', 'telephone', 'vin']
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
        #     'surname': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
        #     'patronymic': forms.TextInput(attrs={'placeholder': 'Отчество'}),
        #     #'telephone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
        #     'vin': forms.TextInput(attrs={'placeholder': 'VIN-номер'}),
        # }

    def clean_car(self):
        car = self.cleaned_data['car']

        if not car:
            message='Значение не может быть Пустым'
            #mess(self.request, message)
            print(car)
            raise forms.ValidationError({"some_field": "raise an error"})
        return car