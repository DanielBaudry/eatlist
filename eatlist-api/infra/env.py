from pydantic import BaseSettings


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
