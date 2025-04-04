from django.urls import path
from . import views

urlpatterns = [
    path('servicos/', views.servicos, name="Serviços"),
    path('servicos/<int:pk>/', views.get_servico, name="Serviços"),
    path('agendamentos/', views.agendamentos, name="Agendamento"),
    path('agendamentos/<int:pk>', views.get_agendamento, name="Agendamento"),
]