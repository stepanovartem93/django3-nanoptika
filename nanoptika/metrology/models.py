from django.db import models

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
    name = models.CharField(verbose_name='Наименование СИ', max_length=128)
    type_of_measurment = models.ForeignKey(TypeOfMeasurment, verbose_name='Тип измерений', on_delete=models.CASCADE)
    state_register_number = models.CharField(verbose_name='ГРСИ №', max_length=16)
    accuracy = models.TextField(verbose_name='Погрешность', max_length=256, default='-')
    factory_number = models.CharField(verbose_name='Заводской номер', max_length=16)
    expluatation_place = models.CharField(verbose_name='Место эксплуатации', max_length=128)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='in_storage')


    def __str__(self):
        return f'{self.name}'

# class CalibrationResult(models.Model):