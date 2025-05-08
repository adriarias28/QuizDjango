from .models import Pacientes, Especialidades, Doctores, Citas, DoctoresEspecialidades
from rest_framework import serializers

class PacientesSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Pacientes
        fields = '__all__'
        
    def validate_nombre(self,value):
        if len (value) < 2:
            raise serializers.ValidationError("El nombre del paciente tiene que tener más de dos caracteres")
    
    def validate_edad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La edad debe ser un número positivo.")
        
class EspecialidadesSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model=Especialidades
        fields = '__all__'
        
class DoctoresSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Doctores
        fields = '__all__'
        
    def validate_anhosExperiencia(self, value):
        if value <= 3:
            raise serializers.ValidationError("Tiene que tener 3 o más años de experiencia")
        
    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre tiene que tener más de 3 caracteres")
        
class CitasSerializer(serializers.ModelSerializer):
    doctores=DoctoresSerializer(read_only=True)
    doctores_id= serializers.PrimaryKeyRelatedField(queryset=Doctores.objects.all(), source='doctores', write_only=True)
    pacientes=PacientesSerializer(read_only=True)
    pacientes_id= serializers.PrimaryKeyRelatedField(queryset=Pacientes.objects.all(), source='pacientes', write_only=True)
    class Meta: 
        model=Citas
        fields = '__all__'
    
    def validate_motivo(self,value):
        if len(value) < 10: 
            raise serializers.ValidationError("La descripción tiene que ser mayor o igual de 10 caracteres")
        return value
        
class DoctoresEspecialidadesSerializer(serializers.ModelSerializer):
    doctores=DoctoresSerializer(read_only=True)
    doctores_id= serializers.PrimaryKeyRelatedField(queryset=Doctores.objects.all(), source='doctores', write_only=True)
    especialidades=EspecialidadesSerializer(read_only=True)
    especialidades_id= serializers.PrimaryKeyRelatedField(queryset=Especialidades.objects.all(), source='especialidades', write_only=True)
    class Meta: 
        model=DoctoresEspecialidades
        fields = '__all__'

