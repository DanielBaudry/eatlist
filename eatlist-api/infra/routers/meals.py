from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from infra.database.conf import get_session
from infra.database.models.meal_sql import MealSQL
from domain.entities.meal import MealWithItems

router = APIRouter(
    prefix="/meals",
    tags=["meals"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[MealWithItems])
def read_meals(session: Session = Depends(get_session)):
    meals = session.exec(select(MealSQL)).all()
    return meals
