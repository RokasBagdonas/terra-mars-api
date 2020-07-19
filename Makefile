install: build migrate

build:
	docker-compose build

up:
	docker-compose up

migrate:
	docker-compose run --rm web python manage.py migrate
	docker-compose down

makemigrations:
	docker-compose run --rm web python manage.py makemigrations
	docker-compose down

down:
	docker-compose down

#utility: removes all images and containers related to terra-mars-api and <none>
clear:
	 docker-compose down && docker images -a | egrep "<none>|terra-mars-api*" | awk '{print $3}' | xargs docker rmi

collectstatic:
	docker-compose run web python manage.py collectstatic
	docker-compose down

dtest = docker-compose -f docker-compose.test.yml 
test:
	$(dtest) build && \
		$(dtest) run --rm web pytest
