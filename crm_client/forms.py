from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Case, When, Value, IntegerField
from django.utils.safestring import mark_safe

from crm_client.models import *
from crm_client.views import *



class AddRecordClient(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
        self.fields['surname'] = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
        self.fields['patronymic'] = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
        self.fields['car'] = forms.ModelChoiceField(empty_label='Марка авто',label=False, required=False, queryset=BrandAuto.objects.exclude(pk=6))
        self.fields['model_car'] = forms.ModelChoiceField(empty_label='Модель авто', label=False, required=False, queryset=ModelAuto.objects.exclude(pk=4))
        self.fields['telephone'] = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
        self.fields['vin'] = forms.CharField(label=False, required=False, widget=forms.TextInput(attrs={'placeholder': 'VIN-номер'}))

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
            raise forms.ValidationError('Поле "Марка авто" не должно быть пустым')
        return car
    #
    # def clean_telephone(self):
    #     telephone = self.cleaned_data['telephone']
    #     if not telephone:
    #         raise forms.ValidationError('Поле "Телефон" не должно быть пустым')
    #     return telephone
    #
    def clean_vin(self):
        vin = self.cleaned_data['vin']
        if not vin:
            raise forms.ValidationError('Поле "VIN" не должно быть пустым')
        return vin

# class AutoClient(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#
#         super().__init__(*args, **kwargs)
#         self.fields['model_brand'] = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={'placeholder': 'Модель автомобиля'}))
#         self.fields['brand'] = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={'placeholder': 'Марка автомобиля'}))
#
#
#     class Meta:
#         model = ModelAuto
#         fields = [ 'brand','model_brand' ]
#
#     def clean_brand(self):
#         brand = self.cleaned_data['brand']
#         if not brand:
#             raise forms.ValidationError('Поле "Марка автомобиля" не должно быть пустым')
#         return brand


# class ModelAutoForm(forms.ModelForm):
#
#     class Meta:
#         model = ModelAuto
#         exclude = ('brand',)
#
#
# class BrandAutoForm(forms.ModelForm):
#
#     class Meta:
#         model = BrandAuto
#         fields = '__all__'


# Форма добавления авто в бд
class AddAutoForm(forms.Form):
    auto_brand = forms.ModelChoiceField(label=mark_safe('<strong>Марка авто</strong>'), empty_label='Выберите марку',
                                        queryset=BrandAuto.objects.none(),)
    add_auto_brand = forms.CharField(label=mark_safe('<strong>Добавить марку автомобиля</strong>'))
    # model = forms.ModelChoiceField(label='Модель авто', empty_label='Выберите модель', queryset=ModelAuto.objects.all())
    add_model = forms.CharField(label=mark_safe('<strong>Добавить модель автомобиля</strong>'))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['add_auto_brand'].required = False
        self.fields['add_model'].required = False
        q_sort = BrandAuto.objects.annotate(
            order=Case(
                When(pk=6, then=Value(1)),
                default=Value(2),
                output_field=IntegerField()
            )
        ).order_by('order', 'auto_brand')
        self.fields['auto_brand'].queryset = q_sort

class SearchClientForm(forms.Form):
    search = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Поиск...'}))


    # def clean_add_auto_brand(self):
    #     add_auto_brand = self.cleaned_data['add_auto_brand']
    #     if not add_auto_brand:
    #         raise forms.ValidationError(mark_safe('<strong>"Добавить марку автомобиля"</strong> Обязательное поле'))
    #     return add_auto_brand
    #
    # def clean_add_model(self):
    #     add_model = self.cleaned_data['add_model']
    #     if not add_model:
    #         raise forms.ValidationError(mark_safe('<strong>"Добавить модель автомобиля"</strong> Обязательное поле'))
    #     return add_model