from django.http import HttpResponse
from django.shortcuts import render
#from django.shortcuts import render
from AppCoder.models import Curso,Profesor,Imagenes,Estudiante,Avatar
from AppCoder.forms import CursoFormulario, ImagenFormulario, LoginForm, ProfesorFormulario, UserRegisterForm,UserEditForm,AvatarForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.1


def curso(self):
    curso = Curso(nombre="Desarrollo Web",comision="19881")
    curso.save()
    documento_de_texto=f"   --->Curso : {curso.nombre} \n Comision: {curso.comision}"
    return HttpResponse(documento_de_texto)


def inicio(request):
    """ return HttpResponse("Vista de inicio") """
    avatar= Avatar.objects.filter(user = request.user.id)
    
    print(avatar[0].imagen.url)
    return render(request, 'AppCoder/inicio.html',{'img':avatar[0].imagen.url })
@login_required
def cursos(request):
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request, 'AppCoder/cursos.html',{"miFormulario":miFormulario})
  # return HttpResponse("Vista de cursos") 
   #return render(request, 'AppCoder/cursos.html')



def estudiantes(request):
    """ return HttpResponse("Vista de estudiantes") """
    return render(request, 'AppCoder/estudiantes.html')



def entregables(request):
    """ return HttpResponse("Vista de entregables") """
    return render(request, 'AppCoder/entregables.html')

'''def cursos(self):
    cursos = Curso.objects.all()
    documento_de_texto=""
    for curso in cursos:
        documento_de_texto+=f"   --->Curso : {curso.nombre} \n Comision: {curso.comision} \n"
    return HttpResponse(documento_de_texto)'''


#VISTA FORMULARIO HTML
""" def cursoFormulario(request):

    if request.method == 'POST':

        nombre = request.POST['curso']
        comision = request.POST['comision']
        curso = Curso(nombre=nombre, comision=comision)

        curso.save()
        return render(request, 'AppCoder/inicio.html')


    return render(request, 'AppCoder/cursoFormulario.html') """

#VISTA DE FORMS DJANGO
""" def cursoFormulario(request):

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request, 'AppCoder/cursoFormulario.html',{"miFormulario":miFormulario}) """

""" 
def profeFormulario(request):

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], 
                                            email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profeFormulario.html',{"miFormulario":miFormulario}) """


def buscarComision(request):
    return render(request, 'AppCoder/buscarComision.html')

def buscar(request):
    #respuesta = f"Estoy buscando la camada nro: {request.GET['comision']}"
    comision=request.GET['comision']
    if comision!="":
        cursos = Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/buscarComision.html',{'cursos':cursos, 'comision':comision})
    else:
         return render(request, 'AppCoder/buscarComision.html',{"error":"No se ingreso una comision"})


def imagenes(request):
    if request.method == 'POST':

        miFormulario = ImagenFormulario(request.POST,request.FILES)
        if miFormulario.is_valid():
            #informacion=miFormulario.cleaned_data
            
            name = miFormulario.cleaned_data.get("nombre")
            img = miFormulario.cleaned_data.get("imagen")
            print(name)
            obj=Imagenes(nombre=name, imagen=img)
            obj.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ImagenFormulario()

    return render(request, 'AppCoder/imagenes.html',{"miFormulario":miFormulario})

def buscarImagens(request):
    nombre=request.GET['nombre']
    if nombre!="":
        imagenes=Imagenes.objects.filter(nombre=request.GET['nombre'])
        return render(request, 'AppCoder/buscarImagen.html',{'imagenes':imagenes ,'nombre':request.GET['nombre']})
    else:
         return render(request, 'AppCoder/buscarImagen.html',{'error':"No se ingreso un nombre"})

def buscarImagen(request):
    return render(request, 'AppCoder/buscarImagen.html')


#CRUD DE PROFESORES
# buscar profesor especifico
#def buscarProfesor(request):
def buscarProfesor(request):
    return render(request, 'AppCoder/buscarProfesor.html')

def buscandoProfesor(request):
    #respuesta = f"Estoy buscando la camada nro: {request.GET['comision']}"
    nombre=request.GET['nombre']
    if nombre!="":
        profesor = Profesor.objects.filter(nombre=nombre)
        return render(request, 'AppCoder/buscarProfesor.html',{'profesor':profesor, 'nombre':nombre})
    else:
         return render(request, 'AppCoder/buscarProfesor.html',{"error":"No se ingreso un profesor"})
@login_required
def profesores(request):
    #return HttpResponse("Vista de profesores")   
    #return render(request, 'AppCoder/profesores.html')
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], 
                                            email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            profesores=Profesor.objects.all()
            return render(request, 'AppCoder/leerProfesores.html',{'profesores':profesores})
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profesores.html',{"miFormulario":miFormulario})

def leerProfesores(request):
    profesores=Profesor.objects.all()
    return render(request, 'AppCoder/leerProfesores.html',{'profesores':profesores})

def eliminarProfesor(request,nombre_profesor):
    profesor = Profesor.objects.get(nombre=nombre_profesor)
    profesor.delete()

    profesores=Profesor.objects.all()
    return render(request, 'AppCoder/leerProfesores.html',{'profesores':profesores})

@login_required
def editarProfesor(request,nombre_profesor):
    
    profesor = Profesor.objects.get(nombre=nombre_profesor)
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            profesor.nombre=informacion['nombre']
            profesor.apellido=informacion['apellido']
            profesor.email=informacion['email']
            profesor.profesion=informacion['profesion']
            profesor.save()

            profesores=Profesor.objects.all()
            return render(request, 'AppCoder/leerProfesores.html',{'profesores':profesores})
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})

    return render(request, 'AppCoder/editarProfesor.html',{"miFormulario":miFormulario,"nombre_profesor":nombre_profesor})

def buscarProfesorID(request,id_profesor):
    profesor = Profesor.objects.get(pk=id_profesor)

    return render(request, 'AppCoder/verProfesor.html',{'profesor':profesor})

#CRUD DE ESTUDIANTES , VISTAS BASADAS EN CLASES

class EstudianteList(ListView,LoginRequiredMixin):
    model = Estudiante
    template_name = 'AppCoder/estudiantes_list.html'
     

class EstudianteDetalle(DetailView,LoginRequiredMixin):
    model = Estudiante
    template_name = 'AppCoder/estudiantes_detalle.html'
    
class EstudianteCreacion(CreateView,LoginRequiredMixin):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido' ,'email']

class EstudianteEdicion(UpdateView,LoginRequiredMixin):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido' ,'email']

class EstudianteEliminar(DeleteView,LoginRequiredMixin):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')


def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'AppCoder/inicio.html',{'form':form,'mensaje':f"Bienvenido {username} "})
            else:
                return render(request, 'AppCoder/login.html',{'form':form,'mensaje':f"Usuario o contraseña incorrectos"})
        else:
            return render(request, 'AppCoder/login.html',{'form':form,'mensaje':f"Formulario invalido"})
    else:
        form = LoginForm()
        return render(request, 'AppCoder/login.html', {'form': form})

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppCoder/inicio.html',{'form_register':form,'mensaje':f"Usuario creado correctamente {username} "})
        else:
            return render(request, 'AppCoder/register.html',{'form_register':form,'mensaje':f"Formulario invalido"})
    else:
        form = UserRegisterForm()
        return render(request, 'AppCoder/register.html', {'form_register': form})
    

@login_required
def editar_Usuario(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            informacion=form.cleaned_data
            request.user.first_name=informacion['first_name']
            request.user.last_name=informacion['last_name']
            request.user.email=informacion['email']
            form.save()
            return render(request, 'AppCoder/inicio.html',{'editarUser':form,'mensaje':f"Usuario editado correctamente",'usuario':request.user})
        else:
            return render(request, 'AppCoder/editarUsuario.html',{'editarUser':form,'mensaje':f"Formulario invalido"})
    else:
        form = UserEditForm(instance=request.user)
        return render(request, 'AppCoder/editarUsuario.html', {'editarUser': form})

def eliminarImagen(request,nombre):
    imagen = Imagenes.objects.get(nombre=nombre)
    imagen.delete()
    return render(request,'AppCoder/inicio.html')

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.get(user=u)
            if avatarViejo!=None:
                avatarViejo.delete()
            
            informacion=form.cleaned_data
            avatar=Avatar(user=u ,imagen=informacion['imagen'])
            avatar.save()
            return render(request, 'AppCoder/inicio.html',{'form_avatar':form,'mensaje':f"Avatar agregado correctamente  "})
        #le saca el de formulario invalido
    else:
        form = AvatarForm()
        return render(request, 'AppCoder/agregarAvatar.html', {'form_avatar': form})

