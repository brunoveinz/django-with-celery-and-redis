from celery import shared_task
import redis

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def test_redis_connection():
    r = redis.Redis(host='redis', port=6379, db=0)
    return r.ping()
