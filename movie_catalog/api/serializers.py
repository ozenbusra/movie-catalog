from dataclasses import field
from unicodedata import category
from rest_framework import serializers
from base.models import ListMovieMapping, Movie, Category, MovieCategoryMapping, MovieList

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class MovieCategoryMappingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    category = CategorySerializer()
    class Meta:
        model = MovieCategoryMapping
        fields = ['movie', 'category']

class MovieCategoryMappingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    category = CategorySerializer()
    class Meta:
        model = MovieCategoryMapping
        fields = ['movie', 'category']

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = ['id', 'list_name']

class ListMovieMappingSerializer(serializers.ModelSerializer):
    list = MovieListSerializer()
    movie = MovieSerializer()

    class Meta:
        model = ListMovieMapping
        fields = ['list', 'movie']