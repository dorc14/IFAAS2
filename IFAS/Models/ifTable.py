from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from Config.db import createEngine

engine = createEngine()
Base = declarative_base()

class IfTable(Base):
    __tablename__ = 'ifs'
    id = Column(String, primary_key=True)
    name = Column(String)
    condition = Column(String)
    if_execute = Column(String)

Base.metadata.create_all(engine)

