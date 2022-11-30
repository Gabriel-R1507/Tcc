from rest_framework import serializers
from src import models

class srcSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'