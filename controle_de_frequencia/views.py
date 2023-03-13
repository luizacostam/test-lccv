from rest_framework import (
    views,
    status
)
from rest_framework.response import Response
from controle_de_frequencia.models import Professor, Disciplinas, Alunos
 
class ProfessorAPIView(views.APIView):
 
    def post(self, request):
        data = request.data
        Professor.objects.crete(
            id_professor=data.get("id_professor"),
            nome=data.get("nome"),
            cpf=data.get("cpf"),
            rg=data.get("rg"),
            codigo=data.get("codigo"),
            email=data.get("email"),
            telefone=data.get("telefone")
        )
 
    def get(self, request):
        data = []
        for prof in Professor.objects.all():
            data.append(dict(
            nome=prof.nome,
            cpf=prof.cpf,
            rg=prof.rg,
            codigo=prof.codigo,
            email=prof.email,
            telefone=prof.telefone
            ))
        return Response(status=status.HTTP_200_OK, data=data)
    
    def update(self, request):
        data = request.data
        params = request.query_params
        id = params.get("id")
        if id:
            professor = Professor.objects.filter(id_professor=id)
            if professor:
                professor = professor.first()
                campos = []
                if data.get("nome"):
                    professor.nome = data.get("nome")
                if data.get("cpf"):
                    professor.cpf = data.get("cpf")
                if data.get("rg"):
                    professor.rg = data.get("rg")
                if data.get("codigo"):
                    professor.codigo = data.get("codigo")
                if data.get("email"):
                    professor.email = data.get("email")
                if data.get("telefone"):
                    professor.telefone = data.get("telefone")
                professor.save()
                return Response(status=status.HTTP_200_OK)
            
        return Response(stauts=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        id = request.query_params.get("id")
        
        if id:
            professor = Professor.objects.filter(id_professor=id)
            if professor:
                professor = professor.first()
                professor.delete()
                return Response(status=status.HTTP_200_OK)
        return Response(stauts=status.HTTP_404_NOT_FOUND)

class DisciplinasAPIView(views.APIView):
    def post(self, request):
        data = request.data
        Disciplinas.objects.create(
            id_disciplina=data.get("id_disciplina"),
            nome=data.get("nome"),
            codigo=data.get("codigo"),
            carga_horaria = data.get("carga_horaria"),
            ementa = data.get("ementa")
        )
        return Response(status=status.HTTP_201_CREATED)
 
    def get(self, request):
        data = []
        for disc in Disciplinas.objects.all():
            data.append(dict(
            nome=disc.nome,
            codigo=disc.codigo,
            carga_horaria = disc.carga_horaria,
            ementa = disc.ementa
            ))
        return Response(status=status.HTTP_200_OK, data=data)
    def update(self, request):
        data = request.data
        params = request.query_params
        id = params.get("id")
        if id:
            disciplinas = Disciplinas.objects.filter(id_disciplina=id)
            if disciplinas:
                disciplinas = disciplinas.first()
                campos = []
                if data.get("nome"):
                    disciplinas.nome = data.get("nome")
                if data.get("codigo"):
                    disciplinas.codigo = data.get("codigo")
                if data.get("carga_horaria"):
                    disciplinas.carga_horaria = data.get("carga_horaria")
                if data.get("ementa"):
                    disciplinas.ementa = data.get("ementa")
                disciplinas.save()
                return Response(status=status.HTTP_200_OK)
            
        return Response(stauts=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        id = request.query_params.get("id")
        
        if id:
            disciplinas = disciplinas.objects.filter(id_disciplinas=id)
            if disciplinas:
                disciplinas = disciplinas.first()
                disciplinas.delete()
                return Response(status=status.HTTP_200_OK)
        return Response(stauts=status.HTTP_404_NOT_FOUND)

class AlunosAPIView(views.APIView):
    def post(self, request):
        data = request.data
        Alunos.objects.create(
            id_aluno=data.get("id_aluno"),
            nome=data.get("nome"),
            cpf=data.get("cpf"),
            rg=data.get("rg"),
            matricula=data.get("matricula"),
            email=data.get("email"),
            telefone=data.get("telefone")
        )
        return Response(status=status.HTTP_201_CREATED)
 
    def get(self, request):
        data = []
        for aluno in Alunos.objects.all():
            data.append(dict(
            nome=aluno.nome,
            cpf=aluno.cpf,
            rg=aluno.rg,
            matricula=aluno.matricula,
            email=aluno.email,
            telefone=aluno.telefone
            ))
        return Response(status=status.HTTP_200_OK, data=data)
    def update(self, request):
        data = request.data
        params = request.query_params
        id = params.get("id")
        if id:
            alunos = Alunos.objects.filter(id_aluno=id)
            if alunos:
                alunos = alunos.first()
                campos = []
                if data.get("nome"):
                    alunos.nome = data.get("nome")
                if data.get("cpf"):
                    alunos.cpf = data.get("cpf")
                if data.get("rg"):
                    alunos.rg = data.get("rg")
                if data.get("matricula"):
                    alunos.matricula = data.get("matricula")
                if data.get("email"):
                    alunos.email = data.get("email")
                if data.get("telefone"):
                    alunos.telefone = data.get("telefone")
                alunos.save()
                return Response(status=status.HTTP_200_OK)
            
        return Response(stauts=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        id = request.query_params.get("id")
        
        if id:
            alunos = alunos.objects.filter(id_aluno=id)
            if alunos:
                alunos = alunos.first()
                alunos.delete()
                return Response(status=status.HTTP_200_OK)
        return Response(stauts=status.HTTP_404_NOT_FOUND)

