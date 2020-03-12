from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Rating
from .serializers import MovieSelializer, RatingSerializer
from django.contrib.auth.models import User


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSelializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        rating_value = int(request.data['stars'])
        if 'stars' in request.data:
             
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = User.objects.get(id=1)
            
            try:
                 rating = Rating.objects.get(user=user.id, movie=movie.id)
                 rating.stars = stars
                 rating.save()
            except:
                 Rating.objects.create(user=user, movie=movie, stars=stars)
            
            if rating_value >= 1 and rating_value <= 5:
                response = {'message': 'its working'}
                return Response(response, status.HTTP_200_OK)
            else:
                response = {'message': 'You need to rate between 1 and 5'}
                return Response(response, status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'You need to provide ratings'}
            return Response(response, status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
