from rest_framework import viewsets
from escola.models import Aluno, Curso
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .serializers import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet): # utiza-se qual do ja exite um modelo a ser trabalhado
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all() # pega todo os objetos de Aluno
    serializer_class = AlunoSerializer # pega classe reponsavel pela serilização de Aluno


class CursosViewSet(viewsets.ModelViewSet): 
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

