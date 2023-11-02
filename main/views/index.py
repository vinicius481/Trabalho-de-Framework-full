

from typing import Any
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

class Index  (View):
        def get (self, request):
            if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')
            return render(request, 'index.html' )