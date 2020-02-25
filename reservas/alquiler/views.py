from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import viewsets

class ServiciosView(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class =ServiciosSerializer






# Create your views here.
