import allure
import random
from src.api_clients.petstore.constants import ErrorMessage


def test_get_pet(petstore_client_v2, create_pet, delete_pet):
    allure.dynamic.title("Тест получения питомца по ID")
    pet = petstore_client_v2.get_pet(pet_id=create_pet["id"], expected_status_code=200)
    print(pet)
    assert pet["id"] == create_pet["id"], "ID питомца не совпадает."
    assert pet["name"] == create_pet["name"], "Имя питомца не совпадает."


def test_check_does_not_exist(petstore_client_v2):
    allure.dynamic.title("Тест получения информации о несуществующем питомце по ID")
    non_existing_id = random.randint(11111111111, 99999999999)
    pet = petstore_client_v2.get_pet(pet_id=non_existing_id, expected_status_code=404)
    assert pet["message"] == ErrorMessage.PET_NOT_FOUND
