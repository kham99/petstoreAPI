import random

import allure
from faker import Faker

faker = Faker()


def test_success_update_pet(petstore_client_v2, create_pet):
    allure.dynamic.title("Тест проверки успешного обновления информации о питомце")
    update_pet_data = {
        "id": create_pet["id"],
        "name": create_pet["name"],
        "status": "available",
        "photoUrls": [faker.url()]
    }
    pet = petstore_client_v2.update_pet(pet_data=update_pet_data, expected_status_code=200)
    assert pet["id"] == create_pet["id"], "ID питомца не совпадает после обновления."
    assert pet["name"] == update_pet_data["name"], "Имя питомца не обновилось."
    assert pet["photoUrls"] == update_pet_data["photoUrls"], "Фото URL питомца не обновилось."


def test_update_incorrect_data(petstore_client_v2):
    allure.dynamic.title("Тест проверки обновления с некорректными данными")
    update_pet_data = {
        "id": random.randint(99999999999999999999999999999, 9999999999999999999999999999999999999999999)
    }
    petstore_client_v2.update_pet(pet_data=update_pet_data, expected_status_code=400)
