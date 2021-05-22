from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import BtcBD
from .plot import *
import sys
from subprocess import run, PIPE

def data():
    table_data = list(BtcBD.objects.all())
    table_data = table_data[-7::]
    return {'data_val': table_data}

def index(request):
    #data = CryptBD.objects.all()[:7]
    return render(request, 'genie/index.html', data())

def external(request):
    start_date = request.POST.get("start_dat")
    end_date = request.POST.get("end_dat")
    if start_date == None: start_date = "2016-11-22"
    if end_date == None: end_date = "2019-03-03"
    plot_inst = Plot(start_date, end_date)
    plot_inst.draw()
    return render(request, 'genie/index.html', data())