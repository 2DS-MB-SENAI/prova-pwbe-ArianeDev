from django.urls import path
from . import views

urlpatterns = [
    path('servicos', views.servicos, name="Serviços"),
    path('servicos/<int:pk>/', views.get_servico, name="Serviços"),
    path('agendamento', views.agendamentos, name="Agendamento"),
    path('agendamento/<int:pk>', views.get_agendamento, name="Agendamento"),
]