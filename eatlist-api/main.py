from fastapi import FastAPI

from infra.database.conf import create_db_and_tables
from infra.routers import items, meals
from infra.env import EnvironmentSettings


conf_env = EnvironmentSettings()

app = FastAPI(
    title=conf_env.APP_NAME,
    version=conf_env.API_VERSION,
)

app.include_router(items.router)
app.include_router(meals.router)


@app.get("/")
async def root():
    return {"message": "Welcome to EatList !"}


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
