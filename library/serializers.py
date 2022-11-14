from rest_framework import serializers
from .models import Book, Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['name', 'note', 'date', 'book', 'featured']


class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Book
        fields = ['title', 'author', 'published', 'genre']


class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published', 'genre']
    
class BookDetailSerializer(serializers.ModelSerializer):
    statuses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    notes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published', 'genre', 'featured', 'readstatuses', 'notes']