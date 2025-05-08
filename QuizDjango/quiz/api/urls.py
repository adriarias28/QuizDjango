from django.urls import path
from.views import PacientesListCreateView, PacientesDetailView, EspecialidadesListCreateView, EspecialidadesDetailView, DoctoresListCreateView, DoctoresDetailView, CitasListCreateView, CitasDetailView, DoctoresEspecialidadesListCreateView, DoctoresEspecialidadesDetailView

urlpatterns = [
    
    path('pacientes/',PacientesListCreateView.as_view(), name='pacientes-lista-crear'),
    path('pacientes/<int:pk>/',PacientesDetailView.as_view(), name='pacientes-editar-actualizar'),
    path('especialidades/',EspecialidadesListCreateView.as_view(), name='especialidades-lista-crear'),
    path('especialidades/<int:pk>/',EspecialidadesDetailView.as_view(), name='especialidades-editar-actualizar'),
    path('doctores/',DoctoresListCreateView.as_view(), name='doctores-lista-crear'),
    path('doctores/<int:pk>/',DoctoresDetailView.as_view(), name='doctores-editar-actualizar'),
    path('citas/',CitasListCreateView.as_view(), name='citas-lista-crear'),
    path('citas/<int:pk>/',CitasDetailView.as_view(), name='citas-editar-actualizar'),
    path('doctoresespecialidad/',DoctoresEspecialidadesListCreateView.as_view(), name='doctoresespecialidad-lista-crear'),
    path('doctoresespecialidad/<int:pk>/',DoctoresEspecialidadesDetailView.as_view(), name='doctoresespecialidad-editar-actualizar')
    
]