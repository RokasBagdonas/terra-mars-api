# terra-mars-api

Web API for returning data about Terraforming Mars games.

## Prerequisites
1. *Docker*
2. *docker-compose*

## How to run using Docker
When in root project directory:

```bash
make install && make up
```
API: `localhost:8000/mars_api/`
Frontend: `localhost:8000`



## Used Technologies
* Backend: _Python Django_ 3.1, _Django Rest Framework_ (3.11), _Postgresql_ (12).
* Utilities: *Dokcer* (19.03), *docker-compose* (1.26), *pytest*, *pytest-factory-boy*
* Frontend: _Vuejs_, Currently Django Rest Framework - api frontend.

---
## Roadmap
- [O] Backend API Setup:
    - [X] Rest Framework
    - [X] Postgres
    - [X] Docker
- [X] Player, Game and PlayerScore views, models, serializers + TDD
- [X] Frontend setup:
    - [X] Webpack
    - [X] Vue3
    - [X] Bulma
- [X] View Games
- [ ] Post Games
- [ ] Login
- [ ] Hosting + CI
- [ ] Player Summary
- [ ] Games' summary stats
- [ ] Latest trends dashboard


## Development
The project is split into to apps: the web api named *mars_api* and the frontend in the `frontend/games`. The `frontend` root dir is a django app that is responsible for initial routing and serving the template. Everything else is done by the generated `webpack-bundle.js`, which is a *Vue* app.

The _mars_\__api_ is app is the backend api for acting on data. Most of the _Makefile_ commands are used to ease the development process.

### Backend
* `make up` - run the API
* `make test` - tests
* `make import_initial_data` - seed the database with initial .csv data

### Frontend
Run from `/frontend/games` dir:
* `yarn install` - installs app dependencies for development.
* `yarn build` - compiles and minifies for production
* `yarn serve` - hot reload server for interactive development. Recommend running this command together with `make up`.
