from sqlalchemy import create_engine

engine = create_engine('sqlite:///mydb.db', echo=True)

print("Connection with SQLite established.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)