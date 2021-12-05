from celery import Celery
from Config.config import redis_url

def createCelery(celeryName):
    celery = Celery(celeryName, broker=redis_url, backend=redis_url)
    return celery