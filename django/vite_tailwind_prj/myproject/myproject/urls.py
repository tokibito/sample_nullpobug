from django.contrib import admin
from django.urls import path
from myapp.views import TopView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TopView.as_view()),
]
