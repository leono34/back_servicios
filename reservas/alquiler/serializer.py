from rest_framework import serializers,viewsets
from .models import *

class ServiciosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Servicios
        fields="__all__"