from django.urls import path

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'model1', views.Model1ViewSet, base_name='model1')

urlpatterns = [
    path('docs/', include_docs_urls(title='app1 API', public=True)),
] + router.urls
