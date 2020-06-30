install: build migrate

build: 
	docker-compose build

up:
	docker-compose up

migrate: 
	docker-compose run --rm web python manage.py migrate

makemigrations: 
	docker-compose run --rm web python manage.py makemigrations


