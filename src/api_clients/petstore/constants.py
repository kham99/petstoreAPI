from enum import StrEnum


class Route(StrEnum):
    PET = "pet"


class ApiVersion(StrEnum):
    V2 = "v2"

class ErrorMessage(StrEnum):
    PET_NOT_FOUND = "Pet not found"

