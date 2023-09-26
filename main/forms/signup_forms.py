from django import forms


class SignupForms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}),
        max_length=30)
    
    password1 =  forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        max_length=30)
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'forms-control', 'placeholder': 'Confirme a senha'}),
        max_length=30)

