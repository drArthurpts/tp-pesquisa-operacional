# forms.py
from django import forms
from .models import Desabrigado

class DesabrigadoForm(forms.ModelForm):
    class Meta:
        model = Desabrigado
        fields = '__all__'  # Certifique-se de que todos os campos obrigatórios estão incluídos