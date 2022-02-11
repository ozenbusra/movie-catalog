from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Category
from api.serializers import CategorySerializer


@api_view(['GET'])
def get_category(request, category_id=None) -> Response:
    category = (
        Category.objects.filter(id=category_id)
        if category_id else Category.objects.all()
    )
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)
