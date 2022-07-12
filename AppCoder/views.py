from django.http import HttpResponse
from django.shortcuts import render
#from django.shortcuts import render
from AppCoder.models import Curso,Profesor,Imagenes,Estudiante
from AppCoder.forms import CursoFormulario, ImagenFormulario, ProfesorFormulario
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.1


def curso(self):
    curso = Curso(nombre="Desarrollo Web",comision="19881")
    curso.save()
    documento_de_texto=f"   --->Curso : {curso.nombre} \n Comision: {curso.comision}"
    return HttpResponse(documento_de_texto)


def inicio(request):
    """ return HttpResponse("Vista de inicio") """
    return render(request, 'AppCoder/inicio.html')

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

#ver esto
def eliminarProfesor(request,nombre_profesor):
    profesor = Profesor.objects.get(nombre=nombre_profesor)
    profesor.delete()

    profesores=Profesor.objects.all()
    return render(request, 'AppCoder/leerProfesores.html',{'profesores':profesores})

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


#CRUD DE ESTUDIANTES , VISTAS BASADAS EN CLASES

class EstudianteList(ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes_list.html'
     

class EstudianteDetalle(DetailView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes_detalle.html'
    
class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido' ]

class EstudianteEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido' ]

class EstudianteEliminar(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')