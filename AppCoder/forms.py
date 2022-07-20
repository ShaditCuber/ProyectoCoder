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
    
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
            }
    )
    )
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        help_text=("Contraseña de al menos 8 caracteres."),
    )
    password2 = forms.CharField(
        label=("Confirmacion Contraseña"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=("Por favor, escribe la misma contraseña anterior."),
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2" ]
        help_texts ={k:"" for k in fields}
        

class UserEditForm(forms.ModelForm):

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    email = forms.EmailField()
    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        
    )
    password2 = forms.CharField(
        label=("Confirmacion Contraseña"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=("Por favor, escribe la misma contraseña anterior."),
    )

    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name', 'password1', 'password2']
        help_texts ={k:"" for k in fields}       

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(label='Nombre de Usuario',widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control"}))
    password = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"form-control"}),
        
    )
    error_messages = {
        "invalid_login": 
            "Por favor, introduzca un nombre de usuario y contraseña correctos. Considere que ambos campos son sensibles al uso de mayúsculas."
        ,
        "inactive": "Esta cuenta esta inactiva.",
    }
    
    class Meta:
        model = User
        fields = ["username", "password","error_messages"]
        help_texts ={k:"" for k in fields}



class AvatarForm(forms.Form):
    imagen=forms.ImageField()
    
    
    