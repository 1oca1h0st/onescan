from celery import shared_task
import requests

@shared_task
def add(x, y):
    result = x + y
    # 通过 webhook 把结果发送回 FastAPI 应用
    webhook_url = 'http://localhost:8000/webhook/task_result/'
    requests.post(webhook_url, json={"task": "add", "result": result})
    return result
