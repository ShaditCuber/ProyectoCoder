from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



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

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=("Contraseña de al menos 8 caracteres."),
    )
    password2 = forms.CharField(
        label=("Confirmacion Contraseña"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=("Por favor, escribe la misma contraseña anterior."),
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2" ]
        help_texts ={k:"" for k in fields}
        
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=("Nombre de usuario"),
        widget=forms.TextInput(attrs={"autofocus": True , "class":""}),
    )
    password = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput,
    )
    class Meta:
        model = User
        fields = ["username", "password"]
        help_texts ={k:"" for k in fields}