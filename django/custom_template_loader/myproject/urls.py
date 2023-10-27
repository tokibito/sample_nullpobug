from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.my_view),
    path('admin/', admin.site.urls),
]
