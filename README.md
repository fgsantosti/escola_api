
# API com Django: Django Rest Framework

O foco aqui é o desenvolvimento de web API's de forma simples e ágil. Segundo a documentação oficial, o Django Rest gera uma API navegável que auxilia na usabilidade para os desenvolvedores. Além disso, possui um sistema de autenticação e serialização dos dados.

## Criando o ambiente virtual


```python
mkdir escola_api
cd escola_escola_api
```


Atualizar o sistema caso esteja no Linux


```python
sudo apt update 
```


```python
sudo apt -y upgrade
```

Instalar o pip3


```python
sudo apt install python3-pip
```

Instalar ferramentas adicionais


```python
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

Instalando o env e virtualenv


```python
sudo apt install -y python3-venv
```


```python
sudo apt install python3-virtualenv
```

Criando seu ambiente virtual. Vamos chamá-lo de generic env


```python
virtualenv env
```

Ative o ambiente virtual 


```python
. env/bin/activate
```

Instalar o framework Django:


```python
pip install django
```

Caso queira desativar o ambiente virtual, na pasta


```python
deactivate 
```


```python
quit()
```

## Preparando o ambiente de desenvolvimento 
Foi instalado inicialmente:
- Pip 3
- Python 3
- Django 3.2.7 (Pode ser instalado no ambiente virtual)
- Virtualenv


1.   https://www.python.org/
2.   https://pip.pypa.io/en/stable/
3.   https://www.djangoproject.com/
4.   https://virtualenv.pypa.io/en/latest/

## Criando o projeto Django Escola Api

Depois de criaremos a pasta seguiremos alguns passos classícos do Django. Dentro da pasta executaremos o seguinte comando:

```python
django-admin startproject setup .
```

`django-admin` é um script que criará os diretórios e arquivos para você. 

manage.py é um script que ajuda com a gestão do site. Com ele, podemos iniciar um servidor de web no nosso computador sem instalar nada, entre outras coisas.

O arquivo `settings.py` contém a configurações do seu site, como a de conexão com o banco de dados. 

O arquivo `urls.py` contém uma lista dos padrões usados por urlresolver.

### Mudando as configurações

Para finalizar a configuração do ambiente, na pasta setup, altere no arquivo settings.py o idioma e o horário que usaremos na aplicação, incluindo as seguintes linhas de código:

```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

### Instalando o Django Rest Framework

A estrutura Django REST é um kit de ferramentas poderoso e flexível para a construção de APIs da Web. Alguns motivos pelos quais você pode querer usar a estrutura REST: 

- A API navegável da Web é uma grande vitória de usabilidade para seus desenvolvedores. 
- Políticas de autenticação, incluindo pacotes para OAuth1a e OAuth2. - Serialização que suporta fontes de dados ORM e não ORM. 
- Totalmente personalizável - basta usar visualizações regulares baseadas em função se você não precisar de recursos mais poderosos. Documentação extensa e ótimo suporte da comunidade. 
- Usado e confiado por empresas internacionalmente reconhecidas, incluindo Mozilla, Red Hat, Heroku e Eventbrite.

Ref. https://www.django-rest-framework.org/

```python
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

Iremos fazer o sistema de uma livraria:

https://lucid.app/lucidchart/invitations/accept/inv_5eed4c07-9e9e-43a9-b319-fb69ce832c6c

Vamos seguir o projeto:

https://github.com/fgsantosti/django_livraria


### Criando uma aplicação

Para manter tudo arrumado, vamos criar uma aplicação separada dentro do nosso projeto. É muito bom ter tudo organizado desde o início.

Vamos criar a aplicação escola com o comando:

```python
python manage.py startapp escola
```

### Realizando a instalação das app's criadas

Depois de criar uma aplicação, também precisamos dizer ao Django que ele deve usá-la. Fazemos isso no arquivo ```setup/settings.py ``` -- abra-o no seu editor de código. Precisamos encontrar o INSTALLED_APPS e adicionar uma linha com 'livraria', logo acima do ].


# Application definition
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #framework
    'escola', #app
]
```



### Criando os modelos para nossa escola

No arquivo ```escola/models.py``` definimos todos os objetos chamados Modelos -- este é um lugar em que vamos definir os relacionamentos entre as classes que estaram presentes na nossa livraria defindos no nosso diagrama e classes.

Vamos abrir ```escola/models.py``` no editor de código, apagar tudo dele e escrever o seguinte código:



```python
from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')) 
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')) 
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

    def __str__(self):
        return self.periodo
```


### Criando tabelas para nossos modelos no banco de dados

O último passo é adicionar nosso novo modelo ao banco de dados. Primeiramente, precisamos fazer com que o Django entenda que fizemos algumas alterações nos nossos modelos.


```python
python manage.py makemigrations escola
```

O Django preparou um arquivo de migração que precisamos aplicar ao nosso banco de dados. 


```python
python manage.py migrate escaola
```

## Django Admin

Para fazermos as operações de 
* Adicionar
* Editar
* Deletar 

Nas tabelas Curso e Aluno que modelamos iremos inicialmente usar o admin do Django. Vamos abrir o arquivo `escola/admin.py`no editor de código e acrescentamos os códigos seguintes.

```python
python manage.py createsuperuser
```

Quando for solicitado, insira seu nome de usuário (letras minúsculas, sem espaços), e-mail e senha. **Não se preocupe por não conseguir ver a senha que está digitando - é assim mesmo**. Digite a senha e aperte a tecla enter para continuar. 

Depois disso, volte ao seu navegador. Faça login com as credenciais de superusuário que você escolheu; você deverá ver o painel de controle de administração do Django.

Logo depois, configure o seu arquivo `escola/admin.py`

```python
from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

# Register your models here.
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 20

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso')
    list_display_links = ('id',)
    list_per_page = 20

admin.site.register(Matricula, Matriculas)

```


Vamos startar o servidor web 


```python
python manage.py runserver #startando o servidor
```

Vamos acessar a área do administrador do sistema que já vem prontinho para gente graças ao framework Django, para isso iremos usamos o segunte endereço no navegador de sua preferência:


```python
http://127.0.0.1:8000/admin/
```


## Serialização 

A estrutura de serialização do Django fornece um mecanismo para “traduzir” os modelos Django para outros formatos. 
Normalmente, esses outros formatos serão baseados em texto e usados para enviar dados do Django por uma conexão, 
mas é possível para um serializador lidar com qualquer formato (baseado em texto ou não). Ref. https://docs.djangoproject.com/en/3.2/topics/serialization/


A primeira coisa que precisamos para começar nossa API da Web é fornecer uma maneira de serializar e desserializar 
s instâncias de snippet em representações como json. Podemos fazer isso declarando serializadores que funcionam de 
forma muito semelhante aos formulários do Django. Crie um arquivo no diretório de escola denominado serializers.py 
(`escola/serializer.py`) e adicione o seguinte código. 

```python
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome',]

```

## Views - Escrevendo visualizações regulares do Django usando nosso Serializer

Vamos ver como podemos escrever algumas visualizações de API usando nossa nova classe Serializer. 
Por enquanto, não usaremos nenhum dos outros recursos do framework REST, apenas escreveremos as visualizações como 
visualizações regulares do Django. Edite o arquivo escola/views.py e adicione o seguinte:

```python
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
```


## Urls - Precisamos conectar essas visualizações

### Suas URLs no Django REST!
É hora de criar nossa primeira URL! 

Queremos que http://127.0.0.1:8000/ seja a página inicial da nossa escola API e exiba uma as urls que configuramos anteriormente.


Abra o arquivo `escola_api/setup/urls.py` no seu editor de código preferido e veja o que aparece:


```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculaCurso


router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculaCurso.as_view())
]

```


Vamos startar o servidor web 


```python
python manage.py runserver #startando o servidor
```


```python
http://127.0.0.1:8000/
```
E você irá vizualizar a página de API Root da nossa escola API. 

