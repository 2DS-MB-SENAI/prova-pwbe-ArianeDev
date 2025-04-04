from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.get_medicos, name="listar_medicos"),
    path('consultas/nova', views.post_consulta, name="criar_consulta"),
]