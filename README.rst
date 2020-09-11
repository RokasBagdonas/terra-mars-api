##############
terra-mars-api
##############

Web API for returning data about Terraforming Mars games.

Prerequisites
=============
1. Docker
2. docker-compose

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
