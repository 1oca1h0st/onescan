from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')


@app.task(name='worker.tasks.process_task')
def process_task(task_id: int):
    print(task_id)
