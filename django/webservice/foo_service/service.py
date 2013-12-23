# coding: utf-8
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.primitive import Integer
from spyne.model.primitive import Unicode
from spyne.model.primitive import DateTime
from spyne.model.complex import Iterable, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication

from django.views.decorators.csrf import csrf_exempt

from myapp import models as myapp_models


class HelloWorldService(ServiceBase):
    @srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(name, times):
        for i in range(times):
            yield u'Hello, %s' % name


class Item(ComplexModel):
    """Itemモデル
    """
    name = Unicode
    value = Integer
    updated_at = DateTime


class ItemService(ServiceBase):
    @srpc(_returns=Iterable(Item))
    def item_all():
        for item in myapp_models.Item.objects.all():
            yield Item(
                name=item.name,
                value=item.value,
                updated_at=item.updated_at)


application = Application(
    [
        HelloWorldService,
        ItemService,
    ],
    tns='foo.example.com',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)


hello_app = csrf_exempt(DjangoApplication(application))
