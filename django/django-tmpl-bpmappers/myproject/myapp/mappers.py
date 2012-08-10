from bpmappers.djangomodel import ModelMapper

from myapp.models import C


class MyMapper(ModelMapper):
    class Meta:
        model = C
