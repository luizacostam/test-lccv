from django.contrib import admin
from django.urls import path
from controle_de_frequencia.views import ProfessorAPIView, DisciplinasAPIView, AlunosAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('professor', ProfessorAPIView.as_view(), name="professor"),
    path('disciplinas', DisciplinasAPIView.as_view(), name="disciplinas"),
    path('alunos', AlunosAPIView.as_view(), name="alunos"),
]
