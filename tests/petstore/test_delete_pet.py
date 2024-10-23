import allure
import random


def test_success_delete_pet(petstore_client_v2, create_pet):
    allure.dynamic.title("Тест проверки успешного удаления питомца по ID")
    petstore_client_v2.delete_pet(pet_id=create_pet["id"], expected_status_code=200)


def test_delete_non_existin_pet(petstore_client_v2):
    allure.dynamic.title("Тест проверки удаления не существующего питомца")
    petstore_client_v2.delete_pet(pet_id=random.randint(1111111111111111111, 9999999999999999999999999),
                                  expected_status_code=404)
