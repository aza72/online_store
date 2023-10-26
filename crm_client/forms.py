from django import forms



class AddRecordClient(forms.Form):
    name = forms.CharField(label="Enter first name",max_length=50)
    surname = forms.CharField()
    patronymic = forms.CharField()
    car = forms.CharField()
    telephone = forms.CharField()
    vin = forms.CharField()
    ord = forms.CharField()
    bonuses = forms.CharField()
    # data_create = forms.DateTimeField(auto_now_add=True, verbose_name='Время создания')