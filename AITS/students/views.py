from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def studentdata(request):
    return HttpResponse("*******Student list with issues********")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework import viewsets
from .models import Studententry
from .serializers import Studententryserializer

class StudententryViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing student instances.
    """
    queryset = Studententry.objects.all()
    serializer_class = Studententryserializer

@api_view(['GET'])
def get_user(request):
    queryset = Studententry.objects.all()
    serializer = Studententryserializer(queryset, many=True)
    return Response(serializer.data )

@api_view(['POST'])
def create_user(request):
        serializer=Studententryserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def queryset_detail(request,pk):
     try:
          user =Studententry.objects.get(pk=pk)
     except Studententry.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
     

     if request.method == 'GET':
          serializer=Studententryserializer(user)
          return Response(serializer.data)
     
     elif request.method == 'PUT':
          serializer =Studententryserializer(user , data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
          return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
     
     elif request.method == 'DELETE':
          user.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)