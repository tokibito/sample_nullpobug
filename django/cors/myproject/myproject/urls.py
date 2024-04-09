from django.contrib import admin
from django.urls import path
from myapp.views import Endpoint

urlpatterns = [
    path('', Endpoint.as_view()),
    path('admin/', admin.site.urls),
]
