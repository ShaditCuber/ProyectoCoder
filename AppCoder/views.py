from django.http import HttpResponse
from django.shortcuts import render
#from django.shortcuts import render
from AppCoder.models import Curso,Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario
# Create your views here.


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
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profesores.html',{"miFormulario":miFormulario})

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
    respuesta = f"Estoy buscando la camada nro: {request.GET['comision']}"
    comision=request.GET['comision']
    if comision!="":
        cursos = Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/resultadosBusqueda.html',{'cursos':cursos, 'comision':comision})
    else:
         return render(request, 'AppCoder/buscarComision.html',{"error":"No se ingreso una comision"})