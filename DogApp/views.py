from django.shortcuts import render
from DogApp.serializers import DogSerializer
from DogApp.models import DogShop
from rest_framework import generics

# Create your views here.
class DogList(generics.ListCreateAPIView):
    queryset = DogShop.objects.all()
    serializer_class = DogSerializer


class DogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = DogShop.objects.all()
    serializer_class = DogSerializer