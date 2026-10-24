from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=[
            "id","title","author","isbn","description","publish_year","available_copies","created_at"
        ]
        read_only_fields=["id","created_at"]