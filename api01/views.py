from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def api01(request):
    return HttpResponse("Hello from API1"
                        "Hello form the Other side \n Hello my dear friend form django ")

