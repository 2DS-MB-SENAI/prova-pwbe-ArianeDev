from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Servico, Agendamento
from .serializer import ServicoSerializer, AgendamentoSerializer 

@api_view(['GET', 'POST'])
def servicos(request):
    if request.method == 'GET':
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_servico(request, pk):
    try:
        servico = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
        return Response({'Error': 'Este serviço não existe'})
    
    serializer = ServicoSerializer(servico)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
def agendamentos(request):
    if request.method == 'GET':
        agendamento = Agendamento.objects.all()
        serializer = AgendamentoSerializer(agendamento, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_agendamento(request, pk):
    try:
        agendamento = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist:
        return Response({'Error': 'Este agendamento não existe'})
    
    serializer = AgendamentoSerializer(agendamento)

    return Response(serializer.data)