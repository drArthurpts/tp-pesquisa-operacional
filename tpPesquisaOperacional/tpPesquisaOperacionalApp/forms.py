from django import forms

class Desabrigado(forms.Form):
    nome = forms.CharField(label=' Nome ', max_length=100)
    idade = forms.IntegerField(label=' Idade')
    sexo = forms.ChoiceField(label=' Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    foto = forms.ImageField(label=' Foto')
    