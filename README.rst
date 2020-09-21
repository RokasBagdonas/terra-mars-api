##############
terra-mars-api
##############

Web API for returning data about Terraforming Mars games.

Prerequisites
=============
1. *Docker*
2. *docker-compose*

How to run using Docker
=======================
When in root project directory:

.. code:: bash

        make install && make up


Can be accessed via :code:`localhost:8000/mars_api/`


Used Technologies
=================
Backend: *Python Django 3.1*, *Django Rest Framework* (3.11), *Postgresql* (12).

Utilities: *Dokcer* (19.03), *docker-compose* (1.26), *pytest*, *pytest-factory-boy*

Frontend: Currently Drst API frontend, **soon** Vuejs.
# frontend


Development
===========
The project is split into to apps: the web api named *mars_api* and the frontend in the `frontend/games`. The `frontend` root dir is a django app that is responsible for initial routing and serving the template. Everything else is done by the generated `webpack-bundle.js`, which is a *Vue* app.


Backend
-------
TODO..


Frontend commands
-----------------
Run from `/frontend/games` dir:
* `yarn install` - installs app dependencies for development.
* `yarn build` - compiles and minifies for production
* `yarn serve` - hot reload server for interactive development. Recommend running this command together with `make up`.
