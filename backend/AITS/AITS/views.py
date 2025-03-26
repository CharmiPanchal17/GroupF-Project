from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from students.serializers import Studententryserializer
from students.models import Studententry

class login(APIView):
    def get(self ,request ,*args ,**kwargs):
        queryset = Studententry.objects.all()
        serializer = Studententryserializer(queryset, many=True)
        return Response(serializer.data) 
        
    
    def post(self ,request ,*args ,**kwargs):
        serializer=Studententryserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

