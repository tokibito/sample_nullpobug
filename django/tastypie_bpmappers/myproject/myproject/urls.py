from django.conf.urls import patterns, include, url
from tastypie.api import Api
from myapp.resources import ItemResource

v1_api = Api(api_name='v1')
v1_api.register(ItemResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
)
