from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header  =  "Lakhman web services admin"
admin.site.site_title  =  "Lakhman web services site"
admin.site.index_title  =  "Lakhman web services Admin"
urlpatterns = [
   path('', views.index, name='home'), path('about', views.about, name='about'),
    path('contacts',    views.contacts,name='contacts'),
    path('services',    views.services,name='services')

]