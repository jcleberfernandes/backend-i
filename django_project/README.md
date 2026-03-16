PROJETO EM DJANGO

Docs Django: https://docs.djangoproject.com/en/6.0/


1 UV VENV 
2 UV INIT
3 UV INSTALL PYTHON 3.14
4 UV PYTHON PIN 3.14
5 UV ADD UVICORN DJANGO
6 UV SYNC



docker ps
docker stop $(docker ps -aq)



uv run django-admin starpoject --help (para saber ferramentas)

uv run django-admin starpoject django_project . (sempre colocar o nome da pasta e o . e para instalar e informar que estou na pasta local)

uv run django-admin starpoject django_project ( sem o ponto e errado, sem o ponto ele duplica a pasta raiz, via dar erros.)


mangegy.py (ficheiro mais importante, nao devemos mexer)

pasta django_project (nome do projeto, poderia ser bananas. dentro dessa pasta esta os ficheiros que o projeto precisa para arrancar.)


