from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from infra.database.conf import get_session
from infra.database.models.item import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


class ItemRead(Item):
    toto: int


@router.get("/")
def read_items(session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    print(items)
    return items


@router.get("/{item_id}")
def read_item(item_id: int, session: Session = Depends(get_session)):
    statement = select(Item).where(Item.id == item_id)
    item = session.exec(statement).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
