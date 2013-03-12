guestbookアプリケーション
=========================

Django1.5で動かせます。

::

   $ mkvirtualenv myproject
   (myproject)$ pip install -r requirements.txt
   (myproject)$ python manaage.py syncdb
   (myproject)$ python manaage.py runserver


jenkins用のビルドコマンド
=========================

django-jenkinsを使ってjenkins用のビルドもできます。

::

   (myproject)$ python manaage.py jenkins  --settings=myproject.settings_jenkins
