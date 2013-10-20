# coding: utf-8
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Item
from myapp.mappers import ItemMapper


@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    return Response(ItemMapper(item).as_dict() for item in items)
