import os
from enum import StrEnum


class Config(StrEnum):
    PET_STORE_BASE_URL = os.getenv("PET_STORE_BASE_URL", "https://petstore.swagger.io")
