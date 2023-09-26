from django.views import View
from django.shortcuts import render, redirect
from ..models import Usuario
from ..forms.updateuser_forms import UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class UpdateUser(LoginRequiredMixin, View):

    template_name = 'update_user.html'

    def get(self, request, pk):
        user = Usuario.objects.get(pk=pk)
        form = UserUpdateForm(instance=user)
        return render(request, self.template_name, {'form': form})


    def post(self, request, pk):
        user = Usuario.objects.get(pk=pk)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            cpf_cnpj = form.cleaned_data['cpf_cnpj']
            email = form.cleaned_data['email']
            if Usuario.objects.filter(cpf_cnpj=cpf_cnpj).exists():
                messages.error(request, 'CPF ou CNPJ já existe')
            elif Usuario.objects.filter(email=email).exists():
                messages.error(request, 'Email já existe')
            else:
                form.save()
                messages.success(request, 'Atualização realizada com sucesso.')

            return redirect('updateuser', pk=pk)
        messages.error(request, 'erro na atualização do cadastro')

        return render(request, self.template_name, {'form': form})
