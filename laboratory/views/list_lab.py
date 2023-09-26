from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from laboratory.models import Laboratory
from django.shortcuts import render, get_object_or_404
from laboratory.forms.schedule_lab_form import ScheduleLabForm


class List_Lab(LoginRequiredMixin, View):

    def get(self, request, pk):
        lab = get_object_or_404(Laboratory, pk=pk)
        form = ScheduleLabForm()
        context = {'lab':lab, 'form': form}
        return render(request, 'list_lab.html', context)
    

    def post(self, request, pk):
        lab = get_object_or_404(Laboratory, pk=pk)
        return render(request, 'list_lab.html', {'lab':lab})