from django.shortcuts import render
from .serializer import CustomUserSerializer
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

@api_view(['POST'])
def post_cadastrar(request):
    nome = request.data.get('username')
    senha = request.data.get('senha')
    phone = request.data.get('phone')
    address = request.data.get('address')
    birth_date = request.data.get('birth_date')
    is_verified = request.data.get('is_verified')

    if not nome or not senha:
        return Response({'Error': 'Os campos senha e nome são obrigatórios!'})
    
    if CustomUser.objects.filter(username=nome).exists():
        return Response({'Error': 'Usuário já existe!'}, status=status.HTTP_400_BAD_REQUEST)
    
    customUser = CustomUser.objects.create_user(
        username=nome,
        password=senha,
        phone=phone,
        address=address,
        birth_date=birth_date,
        is_verified=is_verified
    )

    return Response({'Mensagem': 'Usuário cadastrado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    nome = request.data.get('nome')
    senha = request.data.get('senha')

    user = authenticate(username=nome, password=senha)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        Response({'Erro': 'Digite o usuário e a senha corretos!'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    customUser = CustomUser.objects.all()
    serializer = CustomUserSerializer(customUser, many=True)
    return Response(serializer.data)
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch_profile(request, pk):
    try:
        customUser = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    seralizer = CustomUserSerializer(customUser, data = request.data, partial=True)

    if seralizer.is_valid():
        seralizer.save()
        return Response(seralizer.data, status=status.HTTP_200_OK)
    
    return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)