from typing import Optional
from urllib.parse import urljoin

from src.api_clients.petstore.constants import Route, ApiVersion
from src.base_clients.http_client.client import HTTPClient


class PetStoreAPIClient(HTTPClient):

    def __init__(self, base_url: str, api_version: ApiVersion):
        super().__init__(urljoin(base_url, api_version))

    def get_pet(self, pet_id: int | str, expected_status_code: Optional[int] = None) -> dict:
        response = self.get(path=f"{Route.PET}/{pet_id}", expected_status_code=expected_status_code)
        return response.json()

    def create_pet(self, pet_data: dict, expected_status_code: Optional[int] = None) -> dict:
        response = self.post(path=Route.PET, json=pet_data, expected_status_code=expected_status_code)
        return response.json()

    def delete_pet(self, pet_id: int | str, expected_status_code: Optional[int] = None) -> dict:
        response = self.delete(path=f"{Route.PET}/{pet_id}", expected_status_code=expected_status_code)
        return response.json()

    def update_pet(self, pet_data: dict, expected_status_code: Optional[int] = None) -> dict:
        response = self.put(path=Route.PET, json=pet_data, expected_status_code=expected_status_code)
        return response.json()
