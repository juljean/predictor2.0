from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import CryptBD
from .plot import *
import sys
from subprocess import run, PIPE

def data():
    data = CryptBD.objects.all()[:7]
    return {'data_val': data}

def index(request):
    #data = CryptBD.objects.all()[:7]
    return render(request, 'genie/index.html', data())

def external(request):
    start_date = request.POST.get("start_dat")
    end_date = request.POST.get("end_dat")
    print(start_date, end_date)
    plot_inst = Plot()
    plot_inst.draw()
    return render(request, 'genie/index.html', data())