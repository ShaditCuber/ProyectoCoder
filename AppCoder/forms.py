from django import forms


class CursoFormulario(forms.Form):
        nombre = forms.CharField()
        comision = forms.IntegerField()

class ProfesorFormulario(forms.Form):
        nombre = forms.CharField()
        apellido = forms.CharField()
        email = forms.EmailField()
        profesion = forms.CharField()

class ImagenFormulario(forms.Form):
        nombre = forms.CharField()
        imagen = forms.ImageField()