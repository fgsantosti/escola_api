from django.db.models.query import QuerySet
from rest_framework import permissions
from escola.admin import Alunos
from django.shortcuts import render

from rest_framework import serializers, viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, ListaAlunosMatriculadosSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todos as matriculas"""
    queryset = Matricula.objects.all() 
    serializer_class = MatriculaSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """Exibindo todas as matriculas do aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk']) 
        return queryset
    
    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculaCurso(generics.ListAPIView):
    """Exibindo todos os alunos matriculados por curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]