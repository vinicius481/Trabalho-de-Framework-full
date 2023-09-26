from laboratory.models import Schedule_Lab, Laboratory
from django import forms


class LabInfoWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        if isinstance(value, Laboratory) and value.is_active:
            lab_info = f'numero do laboratório: {value.number_laboratory} nome do laboratório: {value.name_laboratory}'
        else:
            lab_info = 'testando'
    
            return lab_info


class ScheduleLabForm(forms.ModelForm):
    lab_info = forms.CharField(widget=LabInfoWidget, required=False, label='Laboratório')

    class Meta:
        model = Schedule_Lab
        fields = ['lab_info', 'rent_date', 'rent_hour']

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


