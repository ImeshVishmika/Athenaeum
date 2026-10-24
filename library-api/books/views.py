from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Book
from .serializers import BookSerializers

# Create your views here.
#ModelViewSet provides the standard CRUD operations automatically:
#- list() — retrieve books
#- retrieve() — retrieve one book
#- create() — add a book
#- update() — replace a book's fields
#- partial_update() — update selected fields
#- destroy() — delete a book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializers
    permission_classes = [AllowAny]