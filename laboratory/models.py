from django.db import models
from main.models import Usuario
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, time


class Laboratory(models.Model):
    name_laboratory = models.CharField(max_length=20)
    number_laboratory = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    opening_time = models.TimeField(default=datetime.combine(datetime.today(), time(9,0,0)))
    closing_time = models.TimeField(default=datetime.combine(datetime.today(), time(21,0,0)))


    def __str__(self):
        return self.name_laboratory


class Schedule_Lab(models.Model):
    lab = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rent_date = models.DateField() # DATA DO ALUGUEL
    available_hour = models.TimeField() # HORARIO DISPONIVEL
    rent_hour = models.TimeField() #HORARIO DO ALUGUEL
    status = models.CharField(max_length=20, choices=[(1, 'Pendente'), (2, 'Cancelado'), (3, 'Confirmado')], default='1')


    def get_opening_hours_weekend(self):
        day_of_week = self.rent_date.weekday()
        if day_of_week == 5:
            return time(9,0,0), time(14,0,0)
        elif day_of_week == 6:
            return  None, None
        return self.lab.opening_time, self.lab.closing_time

    def clean(self):
        if self.rent_date < timezone.now().date():
            raise ValidationError("A data de aluguel não pode estar no passado.")
        
        opening_time = self.get_opening_hours()
        if opening_time is not None and self.rent_hour >= opening_time:
            raise ValidationError("Laboratório Indisponível")
        
        if (self.available_hour >= self.rent_hour
        or self.lab.opening_time > self.rent_hour 
        or self.lab.closing_time < self.rent_hour
        or not self.lab.is_active
        ):
            raise ValidationError("Laboratório indisponível")
        


    def __str__(self):
        return self.lab.name_laboratory