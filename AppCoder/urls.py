from django.urls import path
from .views import  *
from django.contrib.auth.views import LogoutView


urlpatterns = [
        #path('curso/', curso),
        #name sirve para llamar a la vista sin url
        path('', inicio, name='inicio'),
        path('cursos/', cursos, name='cursos'),
        path('estudiantes/', estudiantes,name='estudiantes'),
        path('profesores/', profesores,name='profesores'),
        path('entregables/', entregables,name='entregables'),
        #path('cursoFormulario/', cursoFormulario,name='cursoFormulario'),
        #path('profeFormulario/', profeFormulario,name='profeFormulario'),
        path('buscarComision/', buscarComision,name='buscarComision'),
        path('buscar/', buscar,name='buscar'),
        path('imagenes/', imagenes,name='imagenes'),
        path('buscarImagen/', buscarImagen,name='buscarImagen'),
        path('buscarImagens/', buscarImagens,name='buscarImagens'),
        path('leerProfesores/', leerProfesores,name='profesores_list'),
        path('eliminarProfesor/<nombre_profesor>', eliminarProfesor,name='eliminarProfesor'),
        path('editarProfesor/<nombre_profesor>', editarProfesor,name='editarProfesor'),
        path('buscarProfesorID/<id_profesor>', buscarProfesorID,name='buscarProfesorID'),
        path('login_request/', login_request,name='login_request'),
        path('register/', register,name='register'),
        path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'),name='logout'),
        #url con CBV
        path('estudiante/list/', EstudianteList.as_view(), name='estudiante_list'),
        path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
        path('estudiante/new/', EstudianteCreacion.as_view(), name='estudiante_new'),
        path('estudiante/editar/<pk>', EstudianteEdicion.as_view(), name='estudiante_edit'),
        path('estudiante/eliminar/<pk>', EstudianteEliminar.as_view(), name='estudiante_delete'),


        path('buscarProfesor/', buscarProfesor,name='buscarProfesor'),
        path('buscandoProfesor/', buscandoProfesor,name='buscandoProfesor'),


        ]