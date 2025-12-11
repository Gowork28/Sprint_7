import pytest
import allure

from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title("Код 200 при успешном логине курьера")
    def test_login_courier_success(self, create_new_courier):
        response = CourierMethods.login_courier(create_new_courier["login"], create_new_courier["password"])
        assert response.status_code == 200
        assert 'id' in response.json()


    @pytest.mark.parametrize("key,value", [
        ("login", ""),
        ("password", "")])
    @allure.title("Код 400 при при попытке логина с пустым полем")
    def test_login_empty_field_data_failed(self, create_new_courier, key, value):
        courier = create_new_courier
        courier[key] = value
        response = CourierMethods.login_courier(courier["login"], courier["password"])
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Код 404 при при попытке логина несуществующего курьера")
    def test_login_non_existing_courier_failed(self, random_valid_courier):
        courier = random_valid_courier
        response = CourierMethods.login_courier(courier["login"], courier["password"])
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @pytest.mark.parametrize("key,value", [
        ("login", "anna"),
        ("password", "12341234")])
    @allure.title("Код 404 при при попытке логина с некорректными данными")
    def test_login_with_wrong_data_failed(self, create_new_courier, key, value):
        courier = create_new_courier
        courier[key] = value
        response = CourierMethods.login_courier(courier["login"], courier["password"])
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
