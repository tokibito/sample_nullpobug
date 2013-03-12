guestbookアプリケーション
=========================

Django1.5で動かせます。

::

   $ mkvirtualenv myproject
   (myproject)$ pip install -r requirements.txt
   (myproject)$ python manage.py syncdb
   (myproject)$ python manage.py runserver


jenkins用のビルドコマンド
=========================

django-jenkinsを使ってjenkins用のビルドもできます。

::

   (myproject)$ python manage.py jenkins --settings=myproject.settings_jenkins
