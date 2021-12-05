from Config.db import createSession
from Models.ifHistoryTable import IfHistoryTable

session = createSession()

def getIfsHistory() -> list:
    ifStats = session.query(IfHistoryTable).all()
    return ifStats

def addIfHistory(date, params: str, result: str):
    newIfHistory = IfHistoryTable(date=date, params=params, result=result)
    session.add(newIfHistory)
    session.commit()
