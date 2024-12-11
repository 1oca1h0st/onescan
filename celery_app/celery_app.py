from celery import Celery

from celery_app.controller.cert import crtsh
from celery_app.controller.nmap import port_scan

app = Celery('tasks',
             broker='pyamqp://user:password@127.0.0.1:5672//',
             backend='rpc://')


@app.task(name='worker.tasks.process_task')
def process_task(task_id: int):
    print(task_id)


@app.task(name='worker.tasks.scan_cert')
def scan_cert(domain: str):
    cert = crtsh()
    result = cert.search(domain)
    if result:
        formatted_result = cert.format_results(result)
        print(formatted_result)


@app.task(name='worker.tasks.nmap_scan')
def nmap_scan(ips: str):
    ip_list = ips.split(',')
    for ip in ip_list:
        print(port_scan(ip))
