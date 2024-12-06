from celery import shared_task
import requests

@shared_task
def sample_task(data):
    # 执行任务
    processed_data = some_processing_function(data)
    # 通过 webhook 把结果发送回 FastAPI 应用
    webhook_url = 'http://localhost:8000/webhook/task_result/'
    requests.post(webhook_url, json={"task": "sample_task", "result": processed_data})
    return processed_data

def some_processing_function(data):
    # 实现任务处理逻辑
    return data  # Placeholder
