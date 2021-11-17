from django.db import models
from django.db.models.fields import URLField

class TypeOfMeasurment(models.Model):
    measurment = models.CharField(verbose_name='Вид измерения', max_length=64, unique=True)

    def __str__(self):
        return f'{self.measurment}'

class MeasuringInstrument(models.Model):
    STATUS_CHOICES = (
        ('in repair', 'В ремонте'),
        ('in work', 'В работе'),
        ('in verification', 'В поверке'),
        ('in calibration', 'На калибровке'),
        ('in storage', 'На хранении'),
    )
    factory_number = models.CharField(verbose_name='Заводской номер', max_length=16)
    name = models.CharField(verbose_name='Наименование СИ', max_length=128)
    type_of_measurment = models.ForeignKey(TypeOfMeasurment, verbose_name='Тип измерений', on_delete=models.CASCADE)
    state_register_number = models.CharField(verbose_name='ГРСИ №', max_length=16)
    expluatation_place = models.CharField(verbose_name='Место эксплуатации', max_length=128)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='in work')
    link_to_fgis = models.URLField(verbose_name='ФГИС "Аршин"', default='https://fgis.gost.ru/fundmetrology/registry/4')


    def __str__(self):
        return f'{self.factory_number}'

class CalibrationResult(models.Model):
    calibration_organisation = models.CharField(verbose_name='Организация-поверитель', max_length=128)
    # name_of_type_mi = models.CharField(verbose_name='Наименование типа СИ', max_length=128)
    # modification_mi = models.CharField(verbose_name='Модификация СИ', max_length=128)
    factory_number = models.ForeignKey(MeasuringInstrument, verbose_name='Заводской номер', on_delete=models.CASCADE)
    calibration_date = models.DateField(verbose_name='Дата проведения поверки/калибровки')
    calibration_date_finish = models.DateField(verbose_name='Дата окончания действия поверки/калибровки')
    document_number = models.CharField(verbose_name='Номер документа', max_length=128)

    def __str__(self):
        return f'{self.factory_number, self.calibration_date_finish, self.document_number}'