from DAL import IFDAL
from BL import IfHistoryBL
import requests
import validators
from tasks.transactionTasks import get_transaction
import re
from Config.addones import Status, externalIfAssUrl, ifAssIfUrl, executeIfAssUrl, makeJsonBody
from logger import logger


def getIf(id: str) -> list:
    newIf = IFDAL.getIf(id)
    return newIf

def getAllIfs() -> list:
    allIfs = IFDAL.getAllIfs()
    return allIfs

def createIf(name: str,properties: str, url: str = None) -> dict:
    body = {
        "name": name,
        "properties":{
            "expression": properties
        },
        "url" : url
    }
    requestBody = makeJsonBody(body)
    if checkIfValidation(name):
        transactionId = requests.post(externalIfAssUrl, json=requestBody).json()["transactionId"]
        result = get_transaction.delay(transactionId)
        transaction = result.get()
        urlBody = checkTransactionStatus(transaction, name, properties)
        WebhookToUrl(url, urlBody)
    else:
        transaction = {
            "error": "There was an error Creating the if, check the name"
        }
    return transaction

def executeIf(name: str, param: str) -> dict:
    id = IFDAL.getIdByName(name)
    body = makeJsonBody(param)
    ifResult = requests.post(externalIfAssUrl + "/" + id + "/execute", json=body).json()
    IfHistoryBL.addIfHistory(param, ifResult["result"])
    return ifResult

def checkIfValidation(name: str) -> bool:
    '''check the if name for creation with this regex'''
    isIfValid = re.search('^[a-z]*[-]+[a-z]+$', name)
    return not IFDAL.checkIfExist(name) and isIfValid

def WebhookToUrl(url: str, body: dict):
    if validators.url(url):
        try:
            requests.post(url, json=body)
        except Exception as exception:
            logger.error("Exception has occured when sending the webhook:", exception)
    else:
        logger.warning("Exception has occured while sending the request:","Wrong Url pls Change")

def checkTransactionStatus(transaction: dict, name:str, properties:str) -> dict:
    if transaction['status'] == Status.SUCCEEDED.name:
        urlBody = ifTransactionSucceeded(transaction, name, properties)
    else:
        urlBody = ifTransactionFailed(transaction)
    return urlBody

def ifTransactionSucceeded(transaction:dict, name:str, properties:str) -> dict:
    id = str(transaction["boxId"])
    executeUrl = ifAssIfUrl + name + executeIfAssUrl
    IFDAL.createIf(id, name, properties, executeUrl)
    transaction['executeUrl'] = executeUrl
    webhookBody = {
        "name": name,
        "url": executeUrl
    }
    return makeJsonBody(webhookBody)

def ifTransactionFailed(transaction:dict) -> dict:
    logger.error("Exception has occured:", transaction["error"])
    webhookBody = {
        "error": transaction["error"]
    }
    return makeJsonBody(webhookBody)