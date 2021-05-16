from django import forms

class UserInput(forms.Form):
    title = forms.CharField(lable='')
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=100)
