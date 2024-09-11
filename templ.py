from typing import List

from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    age: int = Field(..., gt=15, lt=90, description="error disc")
    write: str
    duration: str
    date: date
    genres: List[Genre]


class Bookout(Book):
    id: int