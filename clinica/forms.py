from django import forms
from .models import Consulta

class Forms(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'