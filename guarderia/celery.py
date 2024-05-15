# guarderia/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configurar la ruta de configuración predeterminada para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guarderia.settings')

app = Celery('guarderia')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubrir las tareas desde todas las aplicaciones instaladas
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
