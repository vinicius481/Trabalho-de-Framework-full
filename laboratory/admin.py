from django.contrib import admin
from .models import Laboratory

class CadastroLab(admin.ModelAdmin):
    list_display = ('id', 'name_laboratory', 'number_laboratory', 'is_active',)
    list_display_links = ('name_laboratory', 'number_laboratory')
    search_fields = ('name_laboratory', 'number_laboratory')

# Register your models here.
admin.site.register(Laboratory, CadastroLab)