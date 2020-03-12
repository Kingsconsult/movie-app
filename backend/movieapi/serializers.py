from rest_framework import serializers
from .models import Movie, Rating

class MovieSelializer(serializers.ModelSerializer):
     class Meta:
          model = Movie
          fields = ('id', 'title', 'description', 'price', 'subscription_type', 'cover')

class RatingSerializer(serializers.ModelSerializer):
     class Meta:
          model = Rating
          fields = ('id', 'stars', 'user', 'movie')