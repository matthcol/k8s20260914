from sqlalchemy.orm import Session
from . import models, schemas

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_film = models.Movie(**movie.model_dump())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film

def get_movies(db: Session):
    return db.query(models.Movie).all()

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def set_movie_director(db: Session, movie_id: int, person_id: int):
    movie = get_movie(db, movie_id)
    if movie is None:
        return None
    movie.director_id = person_id
    db.commit()
    db.refresh(movie)
    return movie

def remove_movie_director(db: Session, movie_id: int):
    movie = get_movie(db, movie_id)
    if movie is None:
        return None
    movie.director_id = None
    db.commit()
    db.refresh(movie)
    return movie


def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(**person.model_dump())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def get_persons(db: Session):
    return db.query(models.Person).all()

def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_movies_by_director(db: Session, person_id: int):
    return db.query(models.Movie).filter(models.Movie.director_id == person_id).all()


def get_play(db: Session, movie_id: int, actor_id: int):
    return db.query(models.Play).filter(
        models.Play.movie_id == movie_id,
        models.Play.actor_id == actor_id
    ).first()

def add_actor_to_movie(db: Session, movie_id: int, actor_id: int, play: schemas.PlayCreate):
    db_play = models.Play(movie_id=movie_id, actor_id=actor_id, **play.model_dump())
    db.add(db_play)
    db.commit()
    db.refresh(db_play)
    return db_play

def remove_actor_from_movie(db: Session, movie_id: int, actor_id: int):
    play = get_play(db, movie_id, actor_id)
    if play is None:
        return None
    db.delete(play)
    db.commit()
    return play

def get_movie_cast(db: Session, movie_id: int):
    return db.query(models.Play).filter(models.Play.movie_id == movie_id).all()

def get_person_filmography(db: Session, person_id: int):
    return db.query(models.Play).filter(models.Play.actor_id == person_id).all()
