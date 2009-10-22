from django.conf.urls.defaults import *

import core
core.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'core.views.base_views'),
)
