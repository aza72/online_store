from django import forms
from django.core.exceptions import ValidationError

from crm_client.models import Crm_client, BrandAuto, ModelAuto
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
        self.fields['car'] = forms.ModelChoiceField(empty_label='Марка авто',label=False, required=False, queryset=BrandAuto.objects.all())
        self.fields['model_car'] = forms.ModelChoiceField(empty_label='Модель авто', label=False, required=False, queryset=ModelAuto.objects.all())

        self.fields['telephone'] = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
        self.fields['vin'] =forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'VIN-номер'}))

    class Meta:
        model = Crm_client
        fields = [ 'name', 'surname', 'patronymic', 'car', 'model_car',  'telephone', 'vin']


    def clean(self):
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        patronymic = self.cleaned_data['patronymic']
        if not name and not surname and not patronymic:
            raise forms.ValidationError('Одно из полей "Имя", "Фамилия", "Отчество" должно быть заполнено')
    def clean_car(self):
        car = self.cleaned_data['car']
        if not car:
            raise forms.ValidationError('Поле "Авто" не должно быть пустым')
        return car

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if not telephone:
            raise forms.ValidationError('Поле "Телефон" не должно быть пустым')
        return telephone

    def clean_vin(self):
        vin = self.cleaned_data['vin']
        if not vin:
            raise forms.ValidationError('Поле "VIN" не должно быть пустым')
        return vin

class AutoClient(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['model_brand']= forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={'placeholder': 'Модель автомобиля'}))
        self.fields['brand']=forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Марка автомобиля'}))


    class Meta:
        model = ModelAuto
        fields = [ 'model_brand', 'brand']



