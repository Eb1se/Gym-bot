from __future__ import annotations

import os
from typing import Any

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    __instance = None

    app_name: str
    app_host: str
    app_port: int
    pg_db_host: str
    pg_db_port: int
    pg_db_name: str
    pg_db_login: str
    pg_db_password: str


    def __init__(self, **values: Any):
        super().__init__(**values)
        if not Settings.__instance:
            pass

    @classmethod
    def get_instance(cls) -> Settings:
        if not cls.__instance:
            cls.__instance = Settings()
            cls.version = os.getenv('DOCKER_IMG_VERSION', '0.0.0')
        return cls.__instance

    class Config:
        env_file = ".env"
