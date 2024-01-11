from django.shortcuts import render, HttpResponse
from django.http import HttpResponse


def home(request):

    return render(request, 'calc.html')

def add(request):
    value1 = request.POST['num1']
    value2 = request.POST['num2']
    res = int(value1) + int(value2)
    return render(request, 'result.html', {'res': res})
def about(request):
    return render(request,'base.html')


def contacts(request):
    return render(request, 'forms.py')


def services(request):
    return HttpResponse("this is the services page")


def okGotit(request):
    return HttpResponse("ok gotit page")


def viewServices(request, serviceid):
    return HttpResponse(serviceid)
