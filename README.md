POST: /professor
{
    "id_professor": 1,
    "nome": "luizaa",
    "cpf": "12312312312",
    "rg": "12345678",
    "codigo": "1",
    "email": "luiza@gmail.com",
    "telefone": "82999999999"
}

GET: /professor

PUT: /professor?id=<id>
{
    "nome": "luizaa",
    "cpf": "12312312312",
    "rg": "12345678",
    "codigo": "1",
    "email": "luiza@gmail.com",
    "telefone": "82999999999"
}

DELETE: /professor?id=<id>


POST: /disciplinas
{
    "id_disciplina" = 123,
    "id_professor" = 1,
    "nome" = "professor",
    "codigo" = "12",
    "carga_horaria" = "20",
    "ementa" = "esta é a ementa"
}

GET: /disciplinas

PUT: /disciplinas?id=<id>
{
    "id_professor" = 1,
    "nome" = "professor",
    "codigo" = "12",
    "carga_horaria" = "20",
    "ementa" = "esta é a ementa"
}

DELETE: /disciplinas?id=<id>


POST: /alunos
{
    "id_aluno" = 123,
    "nome" = "luiza",
    "cpf" = "132.321.423-24",
    "rg" = "43234-221",
    "matricula" = "210329-13",
    "telefone" = "(82)99345-9029",
    "email" = "luiza@gmail.com"
}

GET: /alunos

PUT: /alunos?id=<id>
{
    "nome" = "luiza",
    "cpf" = "132.321.423-24",
    "rg" = "43234-221",
    "matricula" = "210329-13",
    "telefone" = "(82)99345-9029",
    "email" = "luiza@gmail.com"
}

DELETE :/alunos?id=<id>
