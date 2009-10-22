# coding:utf8
from core.views import ClassBaseViews, base_views
from django.utils.importlib import import_module

LOADING = False

def autodiscover():
    """
    django.contrib.admin.__init__.autodiscoverとほぼ同じです。
    """
    global LOADING
    if LOADING:
        return
    LOADING = True

    import imp
    from django.conf import settings

    for app in settings.INSTALLED_APPS:
        try:
            app_path = import_module(app).__path__
        except AttributeError:
            continue

        try:
            imp.find_module('action_views', app_path)
        except ImportError:
            continue

        import_module("%s.action_views" % app)

    LOADING = False
