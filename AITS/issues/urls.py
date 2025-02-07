from django.urls import path
from .views import IssueListCreateView, IssueRetrieveUpdateDeleteView

urlpatterns = [
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),  # GET & POST
    path('issues/<int:pk>/', IssueRetrieveUpdateDeleteView.as_view(), name='issue-detail'),  # GET, PUT, DELETE
]
