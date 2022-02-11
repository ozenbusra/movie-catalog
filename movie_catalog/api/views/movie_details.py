from itertools import groupby
from typing import List

from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import utility
from base.models import MovieCategoryMapping
from api.serializers import MovieCategoryMappingSerializer


def get_movies_by_id(movie_id: int):
    return MovieCategoryMapping.objects.order_by('movie_id').filter(movie__movie_id=movie_id)


def get_movies_all():
    return MovieCategoryMapping.objects.order_by('movie_id').all()


def get_movie_queryset(request):
    queryset = get_movies_all()

    if request.GET.get('name'):
        queryset = queryset.filter(
            movie__movie_name__contains=request.GET.get('name').title())

    if request.GET.get('category'):
        queryset = queryset.filter(
            category__category_name__contains=request.GET.get('category').title())

    return queryset


def create_movie_response(movie_list: List) -> List:
    movie_response = []
    def key_func(k): return k.get("movie.movie_id")
    for key, value in groupby(sorted(movie_list, key=key_func),  key_func):
        movie_value = list(value)
        movie = {
            "id": movie_value[0].get('movie.movie_id'),
            "name": movie_value[0].get('movie.movie_name'),
            "categories": [m.get('category.category_name') for m in movie_value]
        }
        movie_response.append(movie)

    return movie_response


@api_view(['GET'])
def get_movie_details(request, movie_id: int = None) -> Response:
    paginator = PageNumberPagination()
    paginator.page = request.GET.get('page', 1)
    paginator.page_size = request.GET.get('size', 20)
    queryset = get_movies_by_id(
        movie_id) if movie_id else get_movie_queryset(request)
    paginated_movies = paginator.paginate_queryset(queryset, request)

    serializer = MovieCategoryMappingSerializer(paginated_movies, many=True)
    movie_list = utility.flatten_movie_list(serializer.data)
    movie_response = create_movie_response(movie_list)

    return paginator.get_paginated_response(movie_response)
