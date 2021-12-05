import requests
from Config.addones import transactionStatus, externalTransactionsUrl
from Config.celeryConfig import createCelery

celery = createCelery('tasks')

@celery.task(name="check_status.task")
def getTransaction(transactionId: str) -> dict:
    transStatus = transactionStatus.PENDING
    while (transStatus == transactionStatus.PENDING):
        transaction = requests.get(externalTransactionsUrl + transactionId).json()
        transStatus = transaction["status"]
    return transaction