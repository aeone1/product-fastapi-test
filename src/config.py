"""
App Settings
"""
import os
import pathlib

from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic import Field, ConfigDict


class BaseSettings(PydanticBaseSettings):
    """"
    https://docs.pydantic.dev/2.5/concepts/pydantic_settings/

    By default, the environment variable name is the same as the field name.

    If you want to change the environment variable name for a single field, you can use an alias.

    There are two ways to do this:
        Using Field(alias=...)
        Using Field(validation_alias=...)
    """
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        extra='allow'


class DatabaseSettings(BaseSettings):
    port: int = Field(default=5432, alias="POSTGRES_PORT")
    name: str = Field(default="product", alias="POSTGRES_DB")
    user: str = Field(default="product", alias="POSTGRES_USER")
    host: str = Field(default="127.0.0.1", alias="POSTGRES_HOST")
    password: str = Field(default="product", alias="POSTGRES_PASSWORD")

    @property
    def dsn(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class UvicornSettings(BaseSettings):
    app: str = "api.main:app"
    port: int = Field(default=8080, alias="PRODUCT_PORT")
    debug: bool = True
    reload: bool = True
    host: str = "0.0.0.0"
    log_level: str = "debug"
    use_colors: bool = True
    proxy_headers: bool = True


class GlobalSettings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
    uvicorn: UvicornSettings = UvicornSettings()


Settings = GlobalSettings()
