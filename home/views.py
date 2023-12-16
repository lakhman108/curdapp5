from django.shortcuts import render, HttpResponse

def index(request):
    contex = {
        'message': 'hello world',
        'message2': 'wow this is great work'
    }
    return render(request, 'index.html', contex)

def about(request):
    return HttpResponse("this is the about page")

def contacts(request):
    return HttpResponse("this is the contanct page")

def services(request):
    return HttpResponse("this is the services page")
