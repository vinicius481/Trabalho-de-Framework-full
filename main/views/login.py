from django.views import View
from django.shortcuts import render, redirect
from ..forms.login_forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from main.models import Usuario


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard.html', username=request.user.username)
        
        form = LoginForm()
        formulario = {'form': form}

        return render(request, 'login.html', formulario)
    
    def post(self, request):
        if request.method == "POST":
            form = LoginForm(request, request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard', username=request.user.username)
                
            else:
                try:
                    user = Usuario.objects.get(username=username)

                    if not user.is_active:
                        raise PermissionDenied('Usuário inativo, entre em contato com o administrador')
                    
                    authenticated_user = authenticate(request, username=username, password=password)

                    if authenticated_user is None:
                        messages.error(request, 'Credenciais Inválida')
                        return render(request, 'login.html', {'form':form})
                    
                except Usuario.DoesNotExist:
                    messages.error(request, 'Usuário não existe')
                    return render(request, 'login.html', {'form':form})
                
                except PermissionDenied as e:
                    messages.error(request, 'Usuário não cadastrado')
                    return render(request, 'login.html', {'form':form})
                
                except Exception as e:
                    messages.error(request, 'Erro desconhecido')
                    return render(request, 'login.html', {'form':form})
        else:
            form = LoginForm()
            formulario = {'form': form}
            return render(request, 'login.html', formulario)