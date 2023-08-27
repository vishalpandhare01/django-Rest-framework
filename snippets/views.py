from django.shortcuts import render

# Create your views here.
from .models import Snippet
from .serializers import SnippetsSerializer
from rest_framework import generics

class SnippetsList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetsSerializer

class SnippetDetail(generics.RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetsSerializer