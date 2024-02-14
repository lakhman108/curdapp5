from django.shortcuts import render


def landing_page(request):
    return render(request, 'index.html')


# Create your views here.
def main_page(request):
    return render(request, 'navbar.html')
