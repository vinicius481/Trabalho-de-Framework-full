from django.views import View
from ..forms.lab_forms import SignupLabForm


class SignupLab(View):
    def get(self, request):
        form = SignupLabForm()
        formulario = {'form': form}