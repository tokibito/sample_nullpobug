app = None


def get_celery_app():
    global app
    import celery
    if app is not None:
        return app
    app = celery.Celery('myproject')
    app.config_from_object('django.conf:settings')
    return app
