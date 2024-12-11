from celery import Celery

from app.core.config import settings

app = Celery('tasks',
             broker=settings.BROKER_URL,
             backend=settings.BACKEND_URL)

app.conf.update({
    'task_routes': {
        'celery_app.tasks.add.add': {'queue': 'add_queue'},
    },
})


def create_task(task_id: int) -> object:
    task = app.send_task('worker.tasks.process_task', args=[task_id])
    return {"status": task.id}


def create_scan_task_cert(domain: str):
    task = app.send_task('worker.tasks.scan_cert', args=[domain])
    return {"status": task.id}


def create_scan_nmap_scan(ips: str):
    task = app.send_task('worker.tasks.nmap_scan', args=[ips])
    return {"status": task.id}
