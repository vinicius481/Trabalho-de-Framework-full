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
            form.save()
            messages.success(request, 'Atualização realizada com sucesso.')

            return redirect('updateuser', pk=pk)

        return render(request, self.template_name, {'form': form})
