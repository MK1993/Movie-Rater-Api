from rest_framework import serializers
from .models import Rating,Movie
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description','no_of_ratings','avg_rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'movie']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        """Create and return a new user."""
        # user = User(username = validated_data['username'],)
        # user.set_password(validated_data['password'])
        # user.save()

        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user