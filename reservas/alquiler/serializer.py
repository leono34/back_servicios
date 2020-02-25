from rest_framework import serializers, viewsets
from .mmodels import *


class ServiciosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Servicios
        field="__all__"