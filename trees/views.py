from django.shortcuts import render
from rest_framework import generics
from .models import Tree
from .serializers import TreeSerializer


class TreeListView(generics.ListAPIView):
    """
    Tree's list
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer


class TreeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Tree's details 
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer  