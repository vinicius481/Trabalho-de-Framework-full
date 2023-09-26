from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from ..models import Usuario
from ..forms.signup_forms import SignupForms
from django.contrib import messages
from django.contrib.auth import login


class Signup(View):
    def get(self, request):
        form = SignupForms()
        data = {'form': form}

        return render(request, 'signup.html', data)
    

    def post(self, request):
        
        form = SignupForms(request.POST)

        if form.is_valid():
            
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print(username)
            print(password1)
            print(password2)

            if password1 == password2:

                user = Usuario.objects.create_user(username=username, password=password1)
                print({'username': username})
                print(f'Recebendo os dados do user do signup.py {user}')
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dashboard', kwargs={'username':username}))
                
                else:
                    print("Usuário não encontrado")
                    messages.error(request, 'Usuário não encontrado.')

            else:
                messages.error(request, 'As senhas não são iguais, tente novamente.')

        else:
            messages.error(request, 'Preencha todos os campos por favor.')

        data = {'form': form}

        return render(request, 'signup.html', data)
    



