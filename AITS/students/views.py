from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def studentdata(request):
    return HttpResponse("*******Student list with issues********")
