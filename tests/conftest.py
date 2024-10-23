import pytest
from config import Config
from src.api_clients.petstore.client import PetStoreAPIClient
from src.api_clients.petstore.constants import ApiVersion
from faker import Faker


@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()


@pytest.fixture(scope="session")
def petstore_client_v2() -> PetStoreAPIClient:
    return PetStoreAPIClient(base_url=Config.PET_STORE_BASE_URL, api_version=ApiVersion.V2)


@pytest.fixture
def create_pet(petstore_client_v2, faker) -> dict:
    pet_data = {
        "name": faker.name(),
        "status": "available",
        "id": "99"
    }
    pet_info = petstore_client_v2.create_pet(pet_data)
    return pet_info


@pytest.fixture
def delete_pet(petstore_client_v2, create_pet):
    yield
    petstore_client_v2.delete_pet(pet_id=create_pet["id"])
