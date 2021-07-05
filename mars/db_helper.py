from django.db import connection


def fetchone(query, *args):
    with connection.cursor() as cursor:
        cursor.execute(query, list(*args))
        row = cursor.fetchone()

    return row
