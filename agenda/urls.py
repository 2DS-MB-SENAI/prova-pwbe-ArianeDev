from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', views.get_servicos, name="Serviços"),
    path('servicos/<int:pk>', views.get_servico, name="Serviços"),
    path('agendamento/', views.get_agendamentos, name="Agendamento"),
    path('agendamento/<int:pk>', views.get_agendamento, name="Agendamento"),
]