from django.urls import path
from DogApp.views import DogList, DogDetails

urlpatterns = [
    path('dogs/', DogList.as_view(), name ='dog-list'),
    path('dogs/<int:pk>/', DogDetails.as_view(), name ='dog-details'),
]