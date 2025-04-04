from django.shortcuts import render, redirect
from .models import Medico, Consulta
from .forms import Forms

def get_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medicos': medicos})

def post_consulta(request):
    if request.method == 'POST':
        form = Forms(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
        
    else:
        form = Forms()

    return render(request, 'forms_consulta.html', {'form': form})
