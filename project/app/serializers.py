from app.models import MovieList
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = "__all__"
