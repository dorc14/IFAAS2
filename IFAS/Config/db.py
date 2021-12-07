from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config.config import sqlite_url

def createEngine():
    engine = create_engine(sqlite_url,connect_args={"check_same_thread": False})
    return engine

def createSession():
    engine = createEngine()
    Session = sessionmaker(bind=engine)
    connection = Session()
    return connection

