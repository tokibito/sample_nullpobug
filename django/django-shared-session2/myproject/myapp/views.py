import json

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        kwargs['session_data'] = json.dumps(
            dict(self.request.session), indent=4, ensure_ascii=False)
        return super().get_context_data(**kwargs)