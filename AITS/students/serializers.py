from rest_framework import serializers
from .models import Studententry

class Studententryserializer(serializers.ModelSerializer):
    class Meta:
        model=Studententry
        fields= '__all__'
