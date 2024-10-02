from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # read = serializers.StringRelatedField(many=True) - Using when you want to return the name related to the user ID, but you can't select it in the read field

    class Meta:
        model = Book
        fields = '__all__'                              # ['id', 'name', 'author', 'publication_date', 'synopsis', 'pages_number', 'isbn_10', 'isbn_13', watched'] 
