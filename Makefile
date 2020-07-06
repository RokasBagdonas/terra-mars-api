install: build migrate

build:
	docker-compose build

up:
	docker-compose up

migrate:
	docker-compose run --rm web python manage.py migrate

makemigrations:
	docker-compose run --rm web python manage.py makemigrations

down:
	docker-compose down

#utility: removes all images and containers related to terra-mars
clear:
	 docker-compose down && docker images -a | egrep "<none>|terra-mars-api*" | awk '{print $3}' | xargs docker rmi
