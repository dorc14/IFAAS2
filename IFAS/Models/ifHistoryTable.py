from sqlalchemy import Column, String, Date
from sqlalchemy.orm import declarative_base
from Config.db import createEngine

engine = createEngine()
Base = declarative_base()

class IfHistoryTable(Base):
    __tablename__ = 'ifHistory'
    date = Column(Date, primary_key=True)
    params = Column(String)
    result = Column(String)

Base.metadata.create_all(engine)