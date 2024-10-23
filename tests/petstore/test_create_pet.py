import allure
from random import randint, uniform
from faker import Faker
import pytest

faker = Faker()


def test_create_a_new_pet(petstore_client_v2):
    allure.dynamic.title("Тест проверки успешного создания питомца с корректными данными")
    create_pet_data = {
        "id": randint(1, 999),
        "name": faker.name(),
        "photoUrls": [faker.url()],
        "status": "available"
    }
    pet = petstore_client_v2.create_pet(pet_data=create_pet_data, expected_status_code=200)
    assert pet["id"] == create_pet_data["id"], "ID питомца не совпадает с заданным при создании"
    assert pet["name"] == create_pet_data["name"], "Имя питомца не совпадает с заданным при создании"
    assert pet["photoUrls"] == create_pet_data["photoUrls"], "Фото URL питомца не совпадает с заданным при создании"
    assert pet["status"] == create_pet_data["status"], "Статус питомца не совпадает с заданным при создании"


@pytest.mark.parametrize("id", [
    randint(-100, -1),
    Faker().lexify(
        text="?" * randint(1, 99),
    ),
    uniform(1.0, 100.0),
    randint(99999999999999999999999999999999999999, 999999999999999999999999999999999999999999999999999)
],
                         )
def test_create_a_new_pet_invalid_id(petstore_client_v2, id):
    allure.dynamic.title("Тест проверки получения ошибки при создании питомца с некорректным ID")
    create_pet_data = {
        "id": id
    }
    pet = petstore_client_v2.create_pet(pet_data=create_pet_data, expected_status_code=405)
    assert pet["id"] == create_pet_data["id"], ("Отправленный ID для создания питомца,"
                                                "и ID созданного питомца не совпадают")


@pytest.mark.parametrize("name", [randint(1, 100), uniform(-99.34, -1.98), False])
def test_create_a_new_pet_incorrect_data_type(petstore_client_v2, name):
    allure.dynamic.title("Тест проверки создания питомца с некорректным типом данных")
    create_pet_data = {
        "name": name
    }
    pet = petstore_client_v2.create_pet(pet_data=create_pet_data, expected_status_code=200)
    assert pet["name"] == create_pet_data["name"], "Имя питомца не совпадает с заданным при создании"
