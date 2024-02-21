from django.contrib import admin
from django.urls import path

from canteen import views

admin.site.site_header  =  "Lakhman web services admin"
admin.site.site_title  =  "Lakhman web services site"
admin.site.index_title  =  "Lakhman web services Admin"
urlpatterns = [
   path('', views.main_page),
   path('newpages/',views.landing_page),
   parh(),

]