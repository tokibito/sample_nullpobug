# coding: utf-8
from django.views.generic import CreateView
from django.core.urlresolvers import reverse

from guestbook.models import Greeting
from guestbook.forms import GreetingForm


class GreetingCreateView(CreateView):
    model = Greeting
    form_class = GreetingForm

    def get_context_data(self, **kwargs):
        kwargs.update(dict(
            greeting_list=Greeting.objects.all(),
        ))
        return kwargs

    def get_success_url(self):
        """成功時のリダイレクト先はguestbook_indexのURL
        """
        return reverse('guestbook_index')
