from django.db.models.query import QuerySet
from escola.admin import Alunos
from django.shortcuts import render

from rest_framework import serializers, viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, ListaAlunosMatriculadosSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todos as matriculas"""
    queryset = Matricula.objects.all() 
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    """Exibindo todas as matriculas do aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk']) 
        return queryset
    
    serializer_class = ListaMatriculaAlunoSerializer

class ListaAlunosMatriculaCurso(generics.ListAPIView):
    """Exibindo todos os alunos matriculados por curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunosMatriculadosSerializer