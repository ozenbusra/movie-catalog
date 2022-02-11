from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base.models import Movie, MovieList, ListMovieMapping
from api.serializers import MovieListSerializer


@api_view(['GET'])
def get_movie_list(request, list_id: int = None) -> Response:
    if list_id:
        movie_list = MovieList.objects.filter(pk=list_id)
    else:
        movie_list = MovieList.objects.all()

    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_movie_list(request) -> Response:
    try:
        movie_list = MovieList.objects.create(
            list_name=request.data.get('list_name'))
        movies = Movie.objects.filter(
            movie_id__in=request.data.get('movie_ids'))

        list_movie_mapping = [
            ListMovieMapping(list=movie_list, movie=movie)
            for movie in movies
        ]

        ListMovieMapping.objects.bulk_create(list_movie_mapping)
        return Response(status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def add_movie_to_list(request, list_id: int = None) -> Response:
    try:
        movie_list = MovieList.objects.get(
            pk=list_id) if list_id else MovieList.objects.get(pk=request.data.get('list_id'))

        movies = Movie.objects.filter(
            movie_id__in=request.data.get('movie_ids'))
        list_movie_mapping = [
            ListMovieMapping(list=movie_list, movie=movie)
            for movie in movies
        ]
        ListMovieMapping.objects.bulk_create(list_movie_mapping)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def remove_movie_from_list(request, list_id: int = None) -> Response:
    try:
        list_id = list_id if list_id else request.data.get('list_id')
        movie_ids = request.data.get('movie_ids')

        ListMovieMapping.objects.filter(list__id=list_id).filter(
            movie__movie_id__in=movie_ids).delete()

        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_movie_list(request, list_id: int = None) -> Response:
    try:
        if list_id:
            MovieList.objects.filter(pk=list_id).delete()
        else:
            MovieList.objects.all().delete()

        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
