from django.views.generic.simple import direct_to_template

from core import base_views

from app2.forms import MyForm

def show_form(request):
    return direct_to_template(request, 'app2/show_form.html', {'form': MyForm()})

base_views.register(show_form, 'form1')
