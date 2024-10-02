from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    # watched = serializers.StringRelatedField(many=True) - Using when you want to return the name related to the user ID, but you can't select it in the watched field
    
    class Meta:
        model = Movie
        fields = '__all__'                                 # ['id', 'name', 'director', 'release_date', 'synopsis', 'watched'] 
    