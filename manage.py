#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time

from django.db import connections
from psycopg2 import OperationalError


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mars.settings.development")
    connect_to_db()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def connect_to_db():
    conn = connections["default"]
    for t in range(0, 10, 2):
        print("connecting to db 📶")
        try:
            conn.connect()
            if conn is not None:
                print("Connected 👌")
                break
            else:
                time.sleep(t)
        except OperationalError:
            print("retrying..")
        finally:
            time.sleep(t)


if __name__ == "__main__":
    main()
