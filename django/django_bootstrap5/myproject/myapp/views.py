from django.views.generic import TemplateView
from . import forms


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        return {'form': forms.MyForm()}
