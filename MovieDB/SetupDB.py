# imports
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Pass a declarative base and create a object to correspond with a table in the database
Base = declarative_base()
    
class Movie(Base):
    
    __tablename__ = 'movie'
    movie_id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    rating = Column(Float)

# Connect to and create the movie table
engine = create_engine("sqlite:///MovieDB//movies_database.db")
Base.metadata.create_all(engine)

# Start a session with the database
# Session = sessionmaker(bind=engine)
# session = Session()
# create a new movie and enter it into the database
# new_movie = Movie(title = "The Shawshank Redemption", rating = 9.2)
# session.add(new_movie)
# session.commit()
# session.close()

