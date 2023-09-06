from rest_framework import viewsets
from colaboradores.api import serializers
from colaboradores import models

class ColaboradoresViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ColaboradoresSerializer
    queryset = models.Colaboradores.objects.all()