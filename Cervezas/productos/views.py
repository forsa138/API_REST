from django.shortcuts import render
from rest_framework import viewsets
from .models import Chela
from .serializers import ChelaSerializer


class ChelaViewSet(viewsets.ModelViewSet):
    serializer_class = ChelaSerializer
    queryset = Chela.objects.all()


