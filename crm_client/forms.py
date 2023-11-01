from django import forms

from crm_client.models import Crm_client, BrandAuto


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
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    patronymic = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    car = forms.ModelChoiceField(empty_label='Авто',label=False, queryset=BrandAuto.objects.all())
    telephone = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    vin = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'VIN-номер'}))


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

class crud_form(forms.Form):
    class Meta:
        model = Crm_client
        fields = ['name', 'surname', 'patronymic', 'car', 'telephone', 'vin']
