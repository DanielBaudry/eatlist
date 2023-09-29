from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from domain.entities.shopping_list import ShoppingListWithItems
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
