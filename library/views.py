from .models import Book, Notes
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import BookSerializer, FeaturedSerializer, NotesSerializer


class BookList(generics.ListCreateAPIView):
    books_queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

class FeaturedList(generics.ListCreateAPIView):
    featured_queryset = Book.objects.filter(featured=True)
    serializer_class = FeaturedSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = FeaturedSerializer(queryset, many=True)
        return Response(serializer.data)

class NotesList(generics.ListCreateAPIView):
    note_queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = NotesSerializer(queryset, many=True)
        return Response(serializer.data)


