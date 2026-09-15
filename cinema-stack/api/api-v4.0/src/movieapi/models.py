from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Movie(Base):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    duration = Column(Integer, nullable=True)  # Duration in minutes
    director_id = Column(Integer, ForeignKey("person.id"), nullable=True)

    director = relationship("Person", back_populates="movies_directed")
    cast = relationship("Play", back_populates="movie", cascade="all, delete-orphan")

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthdate = Column(Date, nullable=True)

    movies_directed = relationship("Movie", back_populates="director")
    filmography = relationship("Play", back_populates="actor", cascade="all, delete-orphan")

class Play(Base):
    __tablename__ = "play"

    movie_id = Column(Integer, ForeignKey("movie.id"), primary_key=True)
    actor_id = Column(Integer, ForeignKey("person.id"), primary_key=True)
    role = Column(String(100), nullable=True)

    movie = relationship("Movie", back_populates="cast")
    actor = relationship("Person", back_populates="filmography")
