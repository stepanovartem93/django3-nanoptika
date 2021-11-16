from django.contrib import admin
from .models import TypeOfMeasurment, MeasuringInstrument

@admin.register(MeasuringInstrument)
class MeasuringInstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_measurment', 'accuracy', 'state_register_number', 
    'factory_number', 'expluatation_place', 'status',)
    list_filter = ('type_of_measurment', 'state_register_number', 'expluatation_place', 'status',)
    search_fileds = ('name','state_register_number',)
    ordering = ('state_register_number', 'status', 'expluatation_place',)
    list_editable = ('status',)



@admin.register(TypeOfMeasurment)
class TypeOfMeasurmentAdmin(admin.ModelAdmin):
    list_display = ('measurment',)