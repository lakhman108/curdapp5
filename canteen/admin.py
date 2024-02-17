from django.contrib import admin
from .models import CustomUser,Service

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', )

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','name','description', )


admin.site.register(Service, ServiceAdmin)