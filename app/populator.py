from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from teamsdb import Base, Teams, Players


engine = create_engine('sqlite:///teamSport.db')
Base.metadata.bind = engine
DB = sessionmaker(bind=engine)
session = DB()

# add team

team1 = Teams(name="Cheetahs", division="one")
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
player1 = Players(name="Ben Parker", status="active", teamName="Cows", position="forward", jerseyNumber= 04)
session.add(player1)

player2 = Players(name="Ken Smith", status="active", teamName="Cows", position="forward", jerseyNumber= 32)
session.add(player2)

player3 = Players(name="Pete Kurn", status="active", teamName="Beavers", position="center", jerseyNumber= 01)
session.add(player3)

player4 = Players(name="Pat Marker", status="injured", teamName="Cheetahs", position="defender", jerseyNumber= 88)
session.add(player4)

session.commit()