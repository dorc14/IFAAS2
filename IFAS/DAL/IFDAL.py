from Config.db import createSession
from Models.ifTable import IfTable

session = createSession()

def getIf(ifId: str) -> list:
    wantedIf = session.query(IfTable).filter(IfTable.id == ifId).all()
    return wantedIf

def getAllIfs() -> list:
    ifs = session.query(IfTable).all()
    return ifs

def createIf(ifId: str, ifName: str, properties: str, executeUrl: str):
    newIf = IfTable(id=ifId, name=ifName, condition=properties, if_execute=executeUrl)
    session.add(newIf)
    session.commit()

def getIdByName(ifName: str) -> list:
    ifId = session.query(IfTable).filter(IfTable.name == ifName).all()
    return ifId["id"]

def checkIfExist(ifName: str) -> bool:
        checkIf = session.query(IfTable).filter(IfTable.name == ifName).all()
        return bool(checkIf)