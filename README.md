# djangocharli

# To build images
docker-compose build

docker-compose run --rm app sh -c "django-admin startproject src ."

docker-compose run --rm app sh -c "python manage.py startapp blog"