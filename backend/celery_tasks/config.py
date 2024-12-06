from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.conf.update({
    'task_routes': {
        'celery_app.tasks.add.add': {'queue': 'add_queue'},
    },
})
