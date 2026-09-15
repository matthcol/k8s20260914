from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    year: int
    duration: int | None = None

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        orm_mode = True
