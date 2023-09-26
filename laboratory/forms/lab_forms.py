from django import forms

class SignupLabForm(forms.Form):
    name_lab = forms.CharField(widget=
        forms.TextInput(
            attrs={'class': 'form-control-lab', 'placeholder': 'Cadastre o Laboratório'}),
            max_length=20)
    
    number_lab = forms.IntegerField(widget=
        forms.NumberInput(
            attrs={'class': 'form-control-lab', 'placeholder': 'Número do Laboratório'}),
            max_length=5)
    
    lab_is_active = forms.BooleanField(widget=
        forms.CheckboxInput(
            attrs={'class': 'form-control-lab', 'placeholder': 'Laboratório Ativo / Desativo'}), required=False)