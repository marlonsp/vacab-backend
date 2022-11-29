from rest_framework import serializers
from .models import Palavra


class PalavraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palavra
        fields = ['id', 'palavra',]

