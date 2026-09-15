from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter()

@router.post("/movies/", response_model=schemas.MovieResponse)
def create_film(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.get("/movies/", response_model=list[schemas.MovieResponse])
def list_films(db: Session = Depends(get_db)):
    return crud.get_movies(db)

@router.get("/movies/{movie_id}", response_model=schemas.MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.put("/movies/{movie_id}/director/{person_id}", response_model=schemas.MovieResponse)
def set_director(movie_id: int, person_id: int, db: Session = Depends(get_db)):
    if crud.get_person(db, person_id) is None:
        raise HTTPException(status_code=404, detail="Person not found")
    movie = crud.set_movie_director(db, movie_id, person_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.delete("/movies/{movie_id}/director", response_model=schemas.MovieResponse)
def unset_director(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.remove_movie_director(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.get("/movies/{movie_id}/actors", response_model=list[schemas.CastMemberResponse])
def list_actors(movie_id: int, db: Session = Depends(get_db)):
    if crud.get_movie(db, movie_id) is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return crud.get_movie_cast(db, movie_id)

@router.post("/movies/{movie_id}/actors/{person_id}", response_model=schemas.CastMemberResponse, status_code=201)
def add_actor(movie_id: int, person_id: int, play: schemas.PlayCreate, db: Session = Depends(get_db)):
    if crud.get_movie(db, movie_id) is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    if crud.get_person(db, person_id) is None:
        raise HTTPException(status_code=404, detail="Person not found")
    if crud.get_play(db, movie_id, person_id) is not None:
        raise HTTPException(status_code=409, detail="Actor already in cast")
    return crud.add_actor_to_movie(db, movie_id, person_id, play)

@router.delete("/movies/{movie_id}/actors/{person_id}", status_code=204)
def remove_actor(movie_id: int, person_id: int, db: Session = Depends(get_db)):
    play = crud.remove_actor_from_movie(db, movie_id, person_id)
    if play is None:
        raise HTTPException(status_code=404, detail="Actor not found in cast")
    return Response(status_code=204)
