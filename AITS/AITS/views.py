from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class login(APIView):
    def get(self ,request ,*args ,**kwargs):
        data ={
            '''Data from the database'''
           ' username':'lecturer'
        }
        return Response(data)