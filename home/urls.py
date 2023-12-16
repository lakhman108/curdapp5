from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header  =  "Lakhman web services admin"
admin.site.site_title  =  "Lakhman web services site"
admin.site.index_title  =  "Lakhman web services Admin"
urlpatterns = [
   path('', views.home, name='home'),
 path('add', views.add, name='add'),
 path('about/', views.about, name='about'),
    path('contacts/',views.contacts,name='contacts'),
    path('services/',views.services,name='services'),
    path('services/<slug:serviceid>', views.viewServices),
    path('okgotit/',views.okGotit,name='okgotit'),
]