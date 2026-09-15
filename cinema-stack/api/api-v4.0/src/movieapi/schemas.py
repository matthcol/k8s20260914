from datetime import date
from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    birthdate: date | None


class PersonCreate(PersonBase):
    pass


class PersonResponse(PersonBase):
    id: int

    class Config:
        orm_mode = True


class PlayBase(BaseModel):
    role: str | None = None


class PlayCreate(PlayBase):
    pass


class CastMemberResponse(PlayBase):
    actor: PersonResponse

    class Config:
        orm_mode = True


class MovieBase(BaseModel):
    title: str
    year: int
    duration: int | None = None
    director_id: int | None = None


class MovieCreate(MovieBase):
    pass


class MovieResponse(MovieBase):
    id: int
    director: PersonResponse | None = None
    cast: list[CastMemberResponse] = []

    class Config:
        orm_mode = True


class FilmographyEntryResponse(PlayBase):
    movie: MovieResponse

    class Config:
        orm_mode = True
