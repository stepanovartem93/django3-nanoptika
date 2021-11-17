from django.contrib import admin
from .models import TypeOfMeasurment, MeasuringInstrument, CalibrationResult

@admin.register(MeasuringInstrument)
class MeasuringInstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_measurment', 'link_to_fgis', 
    'factory_number', 'expluatation_place', 'status',)
    list_filter = ('type_of_measurment', 'name_of_type_mi', 'state_register_number', 'expluatation_place', 'status',)
    search_fields = ('name', 'factory_number', )
    ordering = ('status', 'expluatation_place',)
    list_editable = ('status',)



@admin.register(TypeOfMeasurment)
class TypeOfMeasurmentAdmin(admin.ModelAdmin):
    list_display = ('measurment',)

@admin.register(CalibrationResult)
class CalibrationResult(admin.ModelAdmin):
    list_display = ('calibration_organisation', 'factory_number', 'calibration_date', 'calibration_date_finish', 'document_number')
    search_fields = ('document_number', 'factory_number', )
    
