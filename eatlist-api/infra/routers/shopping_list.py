from datetime import datetime
from typing import List, Annotated

from fastapi import APIRouter, Depends, Body
from sqlmodel import Session, select

from domain.entities.meal import MealForShoppingList, MealBase
from domain.entities.shopping_list import ShoppingListWithItems, UpdateShoppingList
from domain.usecases.add_meal_to_shopping_list import AddMealToShoppingList
from domain.usecases.create_new_shopping_list import CreateNewShoppingList
from infra.database.conf import get_session
from infra.database.models.shopping_list import ShoppingListSQL
from infra.database.repositories.shopping_list import ShoppingListRepoSQL

router = APIRouter(
    prefix="/shoplists",
    tags=["shopping-list"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ShoppingListWithItems])
def read_shopping_lists(session: Session = Depends(get_session)):
    shopping_lists = session.exec(select(ShoppingListSQL)).all()
    return shopping_lists


@router.post("/", status_code=201)
def create_shopping_lists(session: Session = Depends(get_session)):
    shopping_list_repo = ShoppingListRepoSQL(session)
    CreateNewShoppingList(shopping_list_repo=shopping_list_repo).execute()
    return {"response": "ok"}


@router.patch("/{shoplist_id}", status_code=200)
def add_meal_to_shopping_lists(shoplist_id: int, payload: MealForShoppingList, session: Session = Depends(get_session)):
    shopping_list_repo = ShoppingListRepoSQL(session)
    print(payload)
    print(shoplist_id)
    AddMealToShoppingList(shopping_list_repo=shopping_list_repo).execute(
        shoplist_id,
        payload
    )
    return {"response": "ok"}
