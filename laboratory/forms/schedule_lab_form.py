from laboratory.models import Schedule_Lab, Laboratory
from django import forms


class ScheduleLabForm(forms.ModelForm):

    class Meta:
        model = Schedule_Lab
        fields = ['rent_date', 'rent_hour']

    rent_date = forms.DateField(
        label="Dia da Reserva",
        required=True,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type':'date'}
        )
    )

    rent_hour = forms.TimeField(
        label='Horario da Reserva',
        required=True,
        widget=forms.TimeInput(
            attrs={'class': 'form-control', 'type':'time'}
        )
    )