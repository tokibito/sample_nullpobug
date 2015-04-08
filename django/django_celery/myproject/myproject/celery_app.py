def get_celery_app():
    import celery
    app = celery.Celery('myproject')
    app.config_from_object('django.conf:settings')
    return app
