from django.views.generic import View
from ..models import Usuario
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from laboratory.forms.schedule_lab_form import ScheduleLabForm
from laboratory.models import Laboratory


class Dashboard(LoginRequiredMixin, View):

    def get(self, request, username):
        user = get_object_or_404(Usuario, username=username)
        lab_active = Laboratory.objects.filter(is_active=True).values('pk','name_laboratory', 'number_laboratory')
        if lab_active:

            context = {'user': user, 'lab_active': lab_active}

            return render(request, 'dashboard.html', context)
        
        