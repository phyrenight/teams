from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from teamsdb import Base, Teams, Players


engine = create_engine('sqlite:///teamSport.db')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
session = DB()

# add team

team1 = Teams(name="Cheetah", division="one")
session.add(team1)

team2 = Teams(name="Rovers", division="one")
session.add(team2)

team3 = Teams(name="Beavers", division="one")
session.add(team3)

team4 = Teams(name="Farmers", division="one")
session.add(team4)

team5 = Teams(name="Cows", division="one")
session.add(team5)

session.commit()

# add players