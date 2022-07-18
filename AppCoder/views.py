from django.http import HttpResponse
from django.shortcuts import render
#from django.shortcuts import render
from AppCoder.models import Curso,Profesor,Imagenes,Estudiante
from AppCoder.forms import CursoFormulario, ImagenFormulario, ProfesorFormulario, UserRegisterForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.1


def curso(self):
    curso = Curso(nombre="Desarrollo Web",comision="19881")
    curso.save()
    documento_de_texto=f"   --->Curso : {curso.nombre} \n Comision: {curso.comision}"
    return HttpResponse(documento_de_texto)


def inicio(request):
    """ return HttpResponse("Vista de inicio") """
    return render(request, 'AppCoder/inicio.html')
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
        form = AuthenticationForm(request, request.POST)
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
        form = AuthenticationForm()
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
    
