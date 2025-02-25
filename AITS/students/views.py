from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def studentdata(request):
    return HttpResponse("*******Student list with issues********")

from rest_framework import viewsets
from .models import Studententry
from .serializers import Studententryserializer

class StudententryViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing student instances.
    """
    queryset = Studententry.objects.all()
    serializer_class = Studententryserializer