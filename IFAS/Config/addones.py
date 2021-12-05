from enum import Enum
import json

headers = {'Content-Type': 'text/html'}
externalIfAssUrl = "https://ifaas-heroku.herokuapp.com/if"
externalTransactionsUrl = "https://ifaas-heroku.herokuapp.com/transactions/"
ifAssUrl = "http://127.0.0.1:5000/"
ifAssIfUrl = ifAssUrl + 'if/'
executeIfAssUrl = "/execute"

class transactionStatus(Enum):
    SUCCEEDED = "SUCCEEDED"
    PENDING = "PENDING"
    FAILED = "FAILED"

def makeJsonBody(body: dict) -> dict:
    convertJsonToString = json.dumps(body)
    body = json.loads(convertJsonToString)
    return body