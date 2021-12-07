import requests
from Config.celeryConfig import createCelery
from Config.addones import Status, externalTransactionsUrl
from logger import logger

celery = createCelery('transactionTasks')

@celery.task(name="check_status.task")
def get_transaction(transactionId: str) -> dict:
        try:
            transactionStatus = Status.PENDING
            while (transactionStatus == Status.PENDING):
                transaction = requests.get(externalTransactionsUrl + transactionId).json()
                transactionStatus = transaction["status"]
            return transaction
        except Exception as exception:
            logger.error("Exception has occured:", exception)
            raise exception