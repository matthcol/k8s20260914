from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter()


@router.post("/persons/", response_model=schemas.PersonResponse)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db, person)

@router.get("/persons/", response_model=list[schemas.PersonResponse])
def list_persons(db: Session = Depends(get_db)):
    return crud.get_persons(db)

@router.get("/persons/{person_id}", response_model=schemas.PersonResponse)
def get_person(person_id: int, db: Session = Depends(get_db)):
    person = crud.get_person(db, person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.get("/persons/{person_id}/movies-directed", response_model=list[schemas.MovieResponse])
def list_movies_directed(person_id: int, db: Session = Depends(get_db)):
    if crud.get_person(db, person_id) is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return crud.get_movies_by_director(db, person_id)

@router.get("/persons/{person_id}/movies-played", response_model=list[schemas.FilmographyEntryResponse])
def list_filmography(person_id: int, db: Session = Depends(get_db)):
    if crud.get_person(db, person_id) is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return crud.get_person_filmography(db, person_id)
