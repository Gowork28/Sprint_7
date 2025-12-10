import pytest
import allure

from conftest import random_valid_courier
from methods.courier_methods import CourierMethods
from data.test_data import TestDataForCourier

class TestCreateCourier:
    @allure.title("Код 200 при успешном создании курьера")
    def test_create_courier_success(self, random_valid_courier):
        response = CourierMethods.create_courier_data(body = random_valid_courier)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Код 409 при создании курьеров с одинаковыми данными")
    def test_create_similar_courier_failed(self):
        response = CourierMethods.create_courier_data(body = TestDataForCourier.VALID_DATA_FOR_COURIER)
        assert response.status_code == 409

    @pytest.mark.parametrize("key,value", [
        ("login", ""),
        ("password", "")
    ])
    @allure.title("Код 400 при создании курьера с пустым полем ввода")
    def test_create_courier_with_epmty_field(self, random_valid_courier, key, value):
        courier = random_valid_courier
        courier[key]=value
        response = CourierMethods.create_courier_data(body = courier)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


