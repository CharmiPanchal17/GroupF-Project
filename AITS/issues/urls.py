from django.urls import path
from .views import IssueListCreateView, IssueRetrieveUpdateDeleteView, create_issue

urlpatterns = [
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),  # GET & POST
    path('issues/<int:pk>/', IssueRetrieveUpdateDeleteView.as_view(), name='issue-detail'),  # GET, PUT, DELETE


    #Issues End point
    path('issues/create/', create_issue, name='create_issue' ),
]
