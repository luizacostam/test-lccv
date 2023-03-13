import django.db
from django.db import models

class Professor(models.Model):
    id_professor = models.IntegerField()
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    codigo = models.CharField(max_length=8)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)


class Alunos(models.Model):
    id_aluno = models.IntegerField()
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    matricula = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)


class Disciplinas(models.Model):
    id_disciplina = models.IntegerField()
    id_professor = models.IntegerField()
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=7)
    carga_horaria = models.IntegerField()
    ementa = models.TextField()




class DisciplinaAluno(models.Model):
    matricula = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, related_name="disciplina_matricula")
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE, related_name="disciplina_aluno")
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, related_name="aluno_disciplina")
    nota = models.FloatField(default=0.0)



class Frequencia(models.Model):
    id_frequencia = models.IntegerField()
    id_materia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, related_name="materia")
    dia = models.DateField()


class FrequenciaAluno(models.Model):
    id_frequencia_aluno = models.IntegerField()
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE, related_name="aluno")
    id_frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE, related_name="frequencia")
    presenca = models.BooleanField(default=True)


class PlanoAula(models.Model):
    TEORICA = "teorica"
    PRATICA = "pratica"
    TIPO_DE_AULA = [
        (TEORICA, "teorica"),
        (PRATICA, "pratica"),
    ]

    id_plano_aula = models.IntegerField()
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, related_name="disciplina")
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()
    metodo = models.CharField(max_length=50, choices=TIPO_DE_AULA)
    dia = models.DateField()


class Atividades(models.Model):
 
    ATIVIDADE_DE_SALA = "ATIVIDADE_DE_SALA"
    ATIVIDADE_DE_CASA = "ATIVIDADE_DE_CASA"
    PROVA = "PROVA"
    
    TIPO_ATIVIDADES = [
        (ATIVIDADE_DE_SALA, "sala"),
        (ATIVIDADE_DE_CASA, "casa"),
        (PROVA, "prova"),
    ]
 
    id_atividade = models.IntegerField()
    atividade = models.TextField()
    tipo = models.CharField(max_length=50, choices=TIPO_ATIVIDADES)
    data_postagem = models.DateField()
    data_entrega = models.DateField()
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE, related_name="atividade_disciplina")
    id_plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE, related_name="plano_aula")


class AtividadeAluno(models.Model):
    id_atividade_aluno = models.IntegerField()
    id_atividade = models.ForeignKey(Atividades, on_delete=models.CASCADE, related_name="atividade_id")
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE, related_name="atividade_id_aluno")
    nota = models.FloatField()