from django.contrib import admin
from .models import Dossier,Car

# Register your models here.

admin.site.register(Dossier)


class CarAdmin(admin.ModelAdmin):
    list_display = [
        'car_model','year','country','color','mark','car_number'
    ]


admin.site.register(Car,CarAdmin)




