from django.views import View
from django.shortcuts import render, redirect
from ..forms.login_forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


class Login(View):
    def get(self, request):
        form = LoginForm()
        formulario = {'form': form}

        return render(request, 'login.html', formulario)
    
    def post(self, request):
        if request.method == "POST":
            form = LoginForm(request, request.POST)
        #form = LoginForm(request.POST)
        print('PARADA 2')
        
        if form.is_valid():
            print('PARADA 3')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(f'FORMS VALIDADO {username} e {password}')
            print('PARADA 2')

            user = authenticate(request, username=username, password=password)
            print(f'{user}, login.py TESTE')
            print('PARADA 3')

            if user is not None:
                login(request, user)
                return redirect('dashboard', username=request.user.username)
                
            else:
                print("Credenciais inválidas")
                messages.error(request, 'Credenciais invalidas.')
        else:
            form = LoginForm()
            formulario = {'form': form}
            return render(request, 'login.html', formulario)