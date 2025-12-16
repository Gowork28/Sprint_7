import pytest
import allure

from conftest import random_valid_courier
from methods.courier_methods import CourierMethods
from data.test_data import CommonResponses, CreateCourierResponses

class TestCreateCourier:
    @allure.title("Код 200 при успешном создании курьера")
    def test_create_courier_success(self, random_valid_courier):
        with allure.step("Создаем курьера с валидными данными"):
            response = CourierMethods.create_courier_data(body = random_valid_courier)
            assert response.status_code == CommonResponses.CREATED_201["status_code"]
            assert response.json() == CommonResponses.CREATED_201["message"]


    @allure.title("Код 409 при создании курьеров с одинаковыми данными")
    def test_create_similar_courier_failed(self, existing_courier):
        with allure.step("Создаем двух одинаковых курьеров"):
             courier = existing_courier
             response = CourierMethods.create_courier_data(body = courier)
             assert response.status_code == CreateCourierResponses.CONFLICT_409["status_code"]
             assert response.json()["message"] == CreateCourierResponses.CONFLICT_409["message"]


    @pytest.mark.parametrize("key,value", [
        ("login", ""),
        ("password", "")
    ])
    @allure.title("Код 400 при создании курьера с пустым полем ввода")
    def test_create_courier_with_epmty_field(self, random_valid_courier, key, value):
        with allure.step(f"Создаем курьера с пустым полем {key}"):
            courier = random_valid_courier
            courier[key]=value
            response = CourierMethods.create_courier_data(body = courier)
            assert response.status_code == CreateCourierResponses.BAD_REQUEST_400["status_code"]
            assert response.json()["message"] == CreateCourierResponses.BAD_REQUEST_400["message"]


