from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
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


class Players(Base):
    __tablename__ = 'Players'
    pic = Column(String(250))
    player_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    status = Column(String(20), nullable=False)
    position = Column(String(80))
    jerseyNumber = Column(Integer)
    teamName = Column(String(80), ForeignKey('Teams.name'))

engine = create_engine('sqlite:///teamSport.db')

Base.metadata.create_all(engine)
