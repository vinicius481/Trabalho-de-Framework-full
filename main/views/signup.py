# from django.views import View
# from django.shortcuts import render
# from django.urls import reverse
# from django.http import HttpResponseRedirect
# from ..models import Usuario
# from ..forms.signup_forms import SignupForms
# from django.contrib import messages
# from django.contrib.auth import login


# class Signup(View):
#     def get(self, request):
#         form = SignupForms()
#         data = {'form': form}

#         return render(request, 'signup.html', data)
    

#     def post(self, request):
        
#         form = SignupForms(request.POST)

#         if form.is_valid():
            
#             username = form.cleaned_data['username']
#             password1 = form.cleaned_data['password1']
#             password2 = form.cleaned_data['password2']
#             print(username)
#             print(password1)
#             print(password2)

#             if password1 == password2:

#                 if Usuario.objects.filter(username=username).exists():
#                     messages.error(request, 'O nome do usuário já existe')
                
#                 else:
#                     user = Usuario.objects.create_user(username=username, password=password1)
#                     if user is not None:
#                         login(request, user)
#                         return HttpResponseRedirect(reverse('dashboard', kwargs={'username':username}))

#             else:
#                 messages.error(request, 'As senhas não são iguais, tente novamente.')

#         form = {'form': form}

#         return render(request, 'signup.html', form)




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

            if password1 == password2:

                if Usuario.objects.filter(username=username).exists():
                    messages.error(request, 'Usuário já existe')
                
                else:
                    
                    user = Usuario.objects.create_user(username=username, password=password1)

                    if user is not None:
                        user.backend = 'django.contrib.auth.backends.ModelBackend'
                        login(request, user)
                        return HttpResponseRedirect(reverse('dashboard', kwargs={'username':username}))

        form = {'form': form}

        return render(request, 'signup.html', form)
    
