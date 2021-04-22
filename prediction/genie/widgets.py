from django.forms import DateInput

class FengyuanChenDatePickerInput(DateInput):
    template_name = 'widgets/genie/inc/fengyuanchen_datepicker.html'