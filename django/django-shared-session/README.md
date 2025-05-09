# django shared session example

* Python 3.13
* PHP 8.4
* docker compose

## run docker

```
docker compose up
```

open browser and go to `http://localhost/`

# add admin user

```
docker compose exec django python manage.py createsuperuser
```