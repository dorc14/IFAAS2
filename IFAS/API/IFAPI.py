import json
from BL import IFBL
from logger import logger
from http import HTTPStatus

def getAllIfs() -> list:
    try:
        allIfs = IFBL.getAllIfs()
        return allIfs
    except Exception as exception:
        logger.error("Exception has occured:", exception)
        return HTTPStatus.BAD_REQUEST
    except FileNotFoundError as exception:
        logger.error("File Not found:", exception)
        return HTTPStatus.NOT_FOUND
    except ValueError as exception:
        logger.error("Value error:", exception)
        return HTTPStatus.FORBIDDEN

def getIf(ifId: str) -> dict:
    try:
        newIf = IFBL.getIf(ifId)
        return newIf
    except Exception as exception:
        logger.error("Exception has occured:", exception)
        return HTTPStatus.BAD_REQUEST
    except FileNotFoundError as exception:
        logger.error("File Not found:", exception)
        return HTTPStatus.NOT_FOUND
    except ValueError as exception:
        logger.error("Value error:", exception)
        return HTTPStatus.FORBIDDEN

def createIf(body: dict) -> dict:
    try:
        transaction = IFBL.createIf(body["name"], body["condition"], body["url"])
        return json.loads(json.dumps(transaction))
    except Exception as exception:
        logger.error("Exception has occured:", exception)
        return HTTPStatus.BAD_REQUEST
    except FileNotFoundError as exception:
        logger.error("File Not found:", exception)
        return HTTPStatus.NOT_FOUND
    except ValueError as exception:
        logger.error("Value error:", exception)
        return HTTPStatus.FORBIDDEN

def executeIf(name: str, param: str) -> dict:
    try:
        result = IFBL.executeIf(name, param)
        return json.loads(json.dumps(result))
    except Exception as exception:
        logger.error("Exception has occured:", exception)
        return HTTPStatus.BAD_REQUEST
    except FileNotFoundError as exception:
        logger.error("File Not found:", exception)
        return HTTPStatus.NOT_FOUND
    except ValueError as exception:
        logger.error("Value error:", exception)
        return HTTPStatus.FORBIDDEN
