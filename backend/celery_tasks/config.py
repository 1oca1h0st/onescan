from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

app.conf.update({
    'task_routes': {
        'celery_app.tasks.add.add': {'queue': 'add_queue'},
    },
})


def create_task(task_id: int) -> object:
    task = app.send_task('worker.tasks.process_task', args=[task_id])
    return {"status": task.id}
