import coreapi
import coreschema
from rest_framework import viewsets
from rest_framework.schemas import AutoSchema

from .serializers import Model1Serializer
from .models import Model1


class Model1Schema(AutoSchema):
    def get_manual_fields(self, path, method):
        if method not in ['POST', 'PUT', 'PATCH']:
            return []
        return [
            coreapi.Field(
                "data",
                required=False,
                location="form",
                schema=coreschema.Object()
            )
        ]


class Model1ViewSet(viewsets.ModelViewSet):
    serializer_class = Model1Serializer
    queryset = Model1.objects.all()
    schema = Model1Schema()
