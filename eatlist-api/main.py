from datetime import datetime

from fastapi import FastAPI

from infra.database.conf import create_db_and_tables
from infra.database.models.item import Item
from infra.database.models.meal_sql import MealSQL
from infra.database.models.shopping_list import ShoppingListSQL
from infra.routers import items, meals, shopping_list
from infra.env import EnvironmentSettings
from sqlmodel import Session
from infra.database.conf import engine


conf_env = EnvironmentSettings()

app = FastAPI(
    title=conf_env.APP_NAME,
    version=conf_env.API_VERSION,
)

app.include_router(items.router)
app.include_router(meals.router)
app.include_router(shopping_list.router)


@app.get("/")
async def root():
    return {"message": "Welcome to EatList !"}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    items = [
        Item(id=123, name="Pâtes"),
        Item(id=456, name="Pesto"),
        Item(id=789, name="Parmesan"),
    ]
    meal = MealSQL(id=123, name="Pâtes pesto", items=items)

    shoplist = ShoppingListSQL(id=12, date=datetime.utcnow(), items=items)

    with Session(engine) as session:
        session.add(meal)
        session.add(shoplist)
        session.commit()
