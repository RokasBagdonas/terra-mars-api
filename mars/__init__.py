# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from celery import app as celery_app

print("---------- mars.__init__.py ----------")
__all__ = ('celery_app',)
