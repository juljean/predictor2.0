from django import forms
from .widgets import FengyuanChenDatePickerInput

class UserInput(forms.Form):
    title = forms.CharField(lable='')
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=100)

class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%d/%m/%Y'], widget=FengyuanChenDatePickerInput())