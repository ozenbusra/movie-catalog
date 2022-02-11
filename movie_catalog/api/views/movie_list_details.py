from itertools import groupby
from typing import List

from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from base.models import ListMovieMapping
from api.serializers import ListMovieMappingSerializer
from . import utility


def get_movie_lists_by_id(list_id: int):
    return ListMovieMapping.objects.order_by('id').filter(list__id=list_id)


def get_movie_list_queryset(request):
    queryset = ListMovieMapping.objects.all()

    if request.GET.get('name'):
        queryset = queryset.filter(
            list__list_name__contains=request.GET.get('name').title())

    return queryset


def create_movie_list_response(movie_list: List) -> List:
    movie_list_response = []
    def key_func(k): return k.get("list.list_name")
    for key, value in groupby(sorted(movie_list, key=key_func),  key_func):
        movie_value = list(value)
        movie = {
            "id": movie_value[0].get('list.id'),
            "name": movie_value[0].get('list.list_name'),
            "movies": [m.get('movie.movie_name') for m in movie_value]
        }
        movie_list_response.append(movie)

    return movie_list_response


@api_view(['GET'])
def get_movie_list_details(request, list_id: int = None) -> Response:
    paginator = PageNumberPagination()
    paginator.page = request.GET.get('page', 1)
    paginator.page_size = request.GET.get('size', 20)
    queryset = get_movie_lists_by_id(
        list_id) if list_id else get_movie_list_queryset(request)
    paginated_lists = paginator.paginate_queryset(queryset, request)

    serializer = ListMovieMappingSerializer(paginated_lists, many=True)
    movie_list = utility.flatten_movie_list(serializer.data)
    movie_list_response = create_movie_list_response(movie_list)

    return paginator.get_paginated_response(movie_list_response)
