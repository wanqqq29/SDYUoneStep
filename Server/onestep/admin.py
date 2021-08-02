from django.contrib import admin
from onestep.models import Service, tabpanel, card


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('label', 'href', 'color', 'icon', 'type')


# Register your models here.
admin.site.register(Service, ServiceAdmin)
