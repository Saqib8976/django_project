from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("<h1>Hello saqib...!</h1>\n <a target='_blank' href='https://www.youtube.com/'>YOUTUBE</a>")
#
# def index2(request):
#     dynamic = {'name': 'saqib', 'place': 'india'}
#     return render(request, "variable_value_sharing.html", dynamic)

def index3(request):
    return render(request,'index.html')

def About_Us(request):
    return render(request,"About_Us.html")