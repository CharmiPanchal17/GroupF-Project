from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Issue
from .serializers import IssueSerializer


# Create your views here.
class IssueListCreateView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

class IssueRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
