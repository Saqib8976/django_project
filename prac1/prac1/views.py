from django.shortcuts import render
from django.http import HttpResponse


# def index2(request):
#     dynamic = {'name': 'saqib', 'place': 'india'}
#     return render(request, "variable_value_sharing.html", dynamic)

def index3(request):
    return render(request,'index.html')

def About_Us(request):
    return render(request,"About_Us.html")