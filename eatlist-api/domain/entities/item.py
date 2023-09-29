from sqlmodel import SQLModel


class ItemBase(SQLModel):
    name: str
