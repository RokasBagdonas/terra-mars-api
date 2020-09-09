# General =====================================================================
install: build migrate

build:
	docker-compose build

up:
	docker-compose up

ddown = docker-compose down --remove-orphans
down:
	$(ddown)

manage:
	docker-compose run --rm web python manage.py $(command)

import_initial_data:
	docker-compose run --rm web python manage.py import_initial_data ./mars_api/data_import/terra-mars-initial-data.csv

# DB ==========================================================================
migrate:
	docker-compose run --rm web python manage.py migrate $(flags);
	$(ddown)

migzero:
	docker-compose run --rm web python manage.py migrate mars_api zero;
	$(ddown)

makemigrations:
	docker-compose run --rm web python manage.py makemigrations;
	$(ddown)

psql:
	docker exec -it terra-mars-api_db_1 psql -h db mars martian

# Testing =====================================================================
dtest = docker-compose -f docker-compose.test.yml

test:
	$(dtest) build && $(dtest) run --rm test-web pytest $(path)

test-player:
	$(dtest) build && $(dtest) run --rm test-web pytest tests/*/test_player.py

shell:
	docker-compose run web python manage.py shell_plus --ipython --print-sql

shell-test:
	$(dtest) run web python manage.py shell_plus --ipython

# Utility =======================================================================
clear:
	 $(ddown) && docker images -a | egrep "<none>|terra-mars-mars-api*" | awk '{print $3}' | xargs docker rmi

collectstatic:
	docker-compose run web python manage.py collectstatic;
	$(ddown)
