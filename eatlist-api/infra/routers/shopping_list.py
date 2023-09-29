from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from domain.entities.shopping_list import ShoppingListWithItems
from infra.database.conf import get_session
from infra.database.models.shopping_list import ShoppingListSQL

router = APIRouter(
    prefix="/shoplists",
    tags=["shopping-list"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[ShoppingListWithItems])
def read_shopping_lists(session: Session = Depends(get_session)):
    shopping_lists = session.exec(select(ShoppingListSQL)).all()
    return shopping_lists
