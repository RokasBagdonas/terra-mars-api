#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time

from django.db import connections
from psycopg2 import OperationalError


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mars.settings.development")

    # if not "--help" in sys.argv:
        # ensure_db_connection()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


def ensure_db_connection():
    conn = connections["default"]
    print("Connecting to db 📶")
    for t in range(1, 10):
        try:
            conn.connect()
            if conn is not None:
                print("Connected 👌")
                break
            else:
                time.sleep(t)
        except OperationalError:
            print(f"[{t}/10] 🔁")
        finally:
            time.sleep(t)


if __name__ == "__main__":
    main()
