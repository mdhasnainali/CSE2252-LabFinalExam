from rest_framework import serializers
from DogApp.models import DogShop

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogShop
        fields = '__all__'
