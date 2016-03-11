from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(80), nullable=False)
    pic = Column(String(80))

class Teams(Base):
   __tablename__ = 'Teams'
   name = Column(String(200), nullable=False)
   rank = Column(Integer)
   id = Column(Integer, primary_key=True)
   division = Column(String(150))


engine = create_engine('sqlite:///teamSport.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()