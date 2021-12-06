from django.shortcuts import render
from .serializers import MovieSerializer,RatingSerializer,UserSerializer
from .models import Movie,Rating
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def rate_movie(self, request, pk=None):
        
        movie= Movie.objects.get(id=pk)
        user= request.user
        stars= request.data['stars']

        if 'stars' in request.data:
            try:
                rating= Rating.objects.get(movie=movie.id,user=user.id)
                rating.stars= stars
                rating.save()
                serializer= RatingSerializer(rating)
                response= {"message":"Rating updated","result":serializer.data}
                return Response(response,status=status.HTTP_200_OK)
            except:
                rating= Rating.objects.create(movie=movie,user=user,stars=stars)
                serializer= RatingSerializer(rating)
                response= {"message":"Rating created","result":serializer.data}
                return Response(response,status=status.HTTP_200_OK)
        else:
            response= {"message":"You need to provide stars!"}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response= {"message":"You can't create rating like that!"}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response= {"message":"You can't update rating like that!"}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]