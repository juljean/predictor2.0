from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import CryptBD
from .plot import *
import sys
from subprocess import run, PIPE

def data():
    data = []
    for old_val in CryptBD.objects.all()[:7]:
        old = str(old_val.date)
        dash1 = old.find("/")
        dash2 = old.find("/", dash1 + 1)
        month = old[:dash1]
        day = old[int(dash1) + 1: dash2]
        new_val = old[-4:] + "-" + month + "-" + day
        old_val.date = new_val
        data.append(old_val)
    return {'data_val': data}

def index(request):
    #data = CryptBD.objects.all()[:7]
    return render(request, 'genie/index.html', data())

def external(request):
    start_date = request.POST.get("start_dat")
    end_date = request.POST.get("end_dat")
    if start_date == None: start_date = "2016-11-22"
    if end_date == None: end_date = "2019-3-3"
    plot_inst = Plot(start_date, end_date)
    plot_inst.draw()
    return render(request, 'genie/index.html', data())