from rest_framework import viewsets
from src.api import serializers
from src import models


class srcViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.srcSerializer
    queryset = models.Paciente.objects.all()