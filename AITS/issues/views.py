from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from .serializers import IssueSerializer
from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status


# Create your views here.
class IssueListCreateView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

class IssueRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]


# Create Issue

@api_view(['POST'])
def create_issue(request):
    serializer = IssueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
