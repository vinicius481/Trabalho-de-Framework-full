from django.contrib import admin
from .models import Usuario

class CadastroAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',)
    list_display_links = ('id', 'username', 'email')
    search_fields = ('username', 'email', 'cpf_cnpj')


# Register your models here.
admin.site.register(Usuario, CadastroAdmin)