from django.shortcuts import render
from django.views.generic import TemplateView
from genie.forms import IndexForm
from genie.models import BtcBD

from .plot import Plot, Data

class IndexView(TemplateView):
    template_name = 'genie/index.html'

    def get(self, request):
        form = IndexForm()
        table_data = Data().getDataRange()[-7::]
        print(table_data)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            Plot(start_date, end_date).draw()

            # Clean screen for form
            form = IndexForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    # def data(self, request):
    #     table_data = Data().getDataRange()[-7::]
    #     print(table_data)
    #     return render(request, self.template_name, {'data_val': table_data})