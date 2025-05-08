from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Pacientes, Especialidades, Doctores, Citas, DoctoresEspecialidades
from .serializers import PacientesSerializer, EspecialidadesSerializer, DoctoresSerializer, CitasSerializer, DoctoresEspecialidadesSerializer

class PacientesListCreateView(ListCreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer
    
class PacientesDetailView(RetrieveUpdateDestroyAPIView):
    queryset =Pacientes.objects.all()
    serializer_class = PacientesSerializer
    
class EspecialidadesListCreateView(ListCreateAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
    
class EspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset =Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
 
class DoctoresListCreateView(ListCreateAPIView):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer   

class DoctoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset =Doctores.objects.all()
    serializer_class = DoctoresSerializer

class CitasListCreateView(ListCreateAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer   

class CitasDetailView(RetrieveUpdateDestroyAPIView):
    queryset =Citas.objects.all()
    serializer_class = CitasSerializer
    
class DoctoresEspecialidadesListCreateView(ListCreateAPIView):
    queryset = DoctoresEspecialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer   

class DoctoresEspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset =DoctoresEspecialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer