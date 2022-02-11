from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Movie
from api.serializers import MovieSerializer


@api_view(['GET'])
def get_movie(request, movie_id: int = None) -> Response:
    movie = Movie.objects.filter(
        movie_id=movie_id) if movie_id else Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)
