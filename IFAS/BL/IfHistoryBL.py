from DAL import IfHistoryDAL
from datetime import date

def addIfHistory(param:str, result:str):
    IfHistoryDAL.addIfHistory(date.today(), param, result)

def getIfsHistory() -> list:
    return IfHistoryDAL.getIfsHistory()

