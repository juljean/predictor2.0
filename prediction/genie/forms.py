from django import forms

# To change teh default type from text to date
class DateInput(forms.DateInput):
    input_type = 'date'

class IndexForm(forms.Form):
    start_date = forms.DateField(widget = DateInput)
    end_date = forms.DateField(widget=DateInput)