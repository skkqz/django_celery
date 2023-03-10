import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quick_publisher.settings')

app = Celery('quick_publisher')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {

    'send-report-every-single-minute': {
        'task': 'publisher.tasks.send_view_count_report',
        'schedule': crontab(), 
    },

}
