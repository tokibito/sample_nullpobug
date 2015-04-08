概要
====

django-celeryを使わないでdjango+celeryを動かす例

Celeryの起動
============

::

  celery -A myproject worker

settingsを切り替える場合は以下のようになる

::

  DJANGO_SETTINGS_MODULE=myproject.other_settings celery -A myproject worker
