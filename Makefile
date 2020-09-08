ddown = docker-compose down

install: build migrate

build:
	docker-compose build

up:
	docker-compose up

down:
	$(ddown) --remove-orphans

manage:
	docker-compose run --rm web python manage.py $(command)

migrate:
	docker-compose run --rm web python manage.py migrate $(flags);
	$(ddown)

migzero:
	docker-compose run --rm web python manage.py migrate mars_api zero;
	$(ddown)

makemigrations:
	docker-compose run --rm web python manage.py makemigrations;
	$(ddown)

#utility: removes all images and containers related to terra-mars-api and <none>
clear:
	 $(ddown) && docker images -a | egrep "<none>|terra-mars-mars-api*" | awk '{print $3}' | xargs docker rmi

collectstatic:
	docker-compose run web python manage.py collectstatic;
	$(ddown)

dtest = docker-compose -f docker-compose.test.yml

test:
	$(dtest) build && $(dtest) run --rm test-web pytest $(path)

test-player:
	$(dtest) build && $(dtest) run --rm test-web pytest tests/*/test_player.py

shell:
	docker-compose run web python manage.py shell_plus --ipython --print-sql

shell-test:
	$(dtest) run web python manage.py shell_plus --ipython

psql:
	docker exec -it terra-mars-api_db_1 psql -h db mars martian
