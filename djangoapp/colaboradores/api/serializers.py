from rest_framework import serializers
from colaboradores import models

class ColaboradoresSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Colaboradores
        fields = '__all__'