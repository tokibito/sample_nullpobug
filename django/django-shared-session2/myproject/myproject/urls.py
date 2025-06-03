from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/', include(('myapp.urls', 'myapp'))),
    path('', RedirectView.as_view(url=reverse_lazy('myapp:home')), name='index'),
]
