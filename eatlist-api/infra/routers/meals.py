from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from infra.database.conf import get_session
from infra.database.models.meal import MealBase, Meal
from infra.database.models.item import Item

router = APIRouter(
    prefix="/meals",
    tags=["meals"],
    responses={404: {"description": "Not found"}},
)


class MealWithItems(MealBase):
    items: List[Item] = []


@router.get("/", response_model=List[MealWithItems])
def read_meals(session: Session = Depends(get_session)):
    meals = session.exec(select(Meal)).all()
    return meals
