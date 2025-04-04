from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.post_cadastrar, name="Cadastrar"),
    path('login/', views.login, name="Logar"),
    path('profile/', views.get_profile),
    path('profile/', views.patch_profile),
]