from django.http import HttpResponse
from django.shortcuts import render

from canteen.models import Service



def landing_page(request):
    return render(request, 'index.html')


# Create your views here.
def main_page(request):
    services_data= Service.objects.all();
    all_data= [];
    for data in services_data:
        dict={
            'service_icon': data.service_icon,
            'service_name': data.name,
            'service_description': data.description
        }
        all_data.append(dict);
        print(dict);
    return render(request, 'navbar.html', {'all_data': all_data})



