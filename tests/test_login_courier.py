import pytest
import allure

from methods.courier_methods import CourierMethods
from data.test_data import CommonResponses, LoginCourierResponses

class TestLoginCourier:

    @allure.title("Код 200 при успешном логине курьера")
    def test_login_courier_success(self, create_new_courier):
        with allure.step("Авторизуемся созданным курьером"):
            response = CourierMethods.login_courier(create_new_courier["login"], create_new_courier["password"])
            assert response.status_code == CommonResponses.OK_200["status_code"]
            assert 'id' in response.json()


    @pytest.mark.parametrize("key,value", [
        ("login", ""),
        ("password", "")])
    @allure.title("Код 400 при при попытке логина с пустым полем")
    def test_login_empty_field_data_failed(self, create_new_courier, key, value):
        with allure.step("Создаем курьера"):
            courier = create_new_courier
        with allure.step(f"Авторизуемся созданным курьером с пустым полем {key}"):
            courier[key] = value
            response = CourierMethods.login_courier(courier["login"], courier["password"])
            assert response.status_code == LoginCourierResponses.BAD_REQUEST_400["status_code"]
            assert response.json()["message"] == LoginCourierResponses.BAD_REQUEST_400["message"]

    @allure.title("Код 404 при при попытке логина несуществующего курьера")
    def test_login_non_existing_courier_failed(self, random_valid_courier):
        with allure.step("Генерируем тестовые данные для курьера"):
            courier = random_valid_courier
        with allure.step("Авторизуемся несуществующим курьером"):
            response = CourierMethods.login_courier(courier["login"], courier["password"])
            assert response.status_code == LoginCourierResponses.NOT_FOUND_404["status_code"]
            assert response.json()["message"] == LoginCourierResponses.NOT_FOUND_404["message"]

    @pytest.mark.parametrize("key,value", [
        ("login", "anna"),
        ("password", "12341234")])
    @allure.title("Код 404 при при попытке логина с некорректными данными")
    def test_login_with_wrong_data_failed(self, create_new_courier, key, value):
        with allure.step("Создаем курьера"):
            courier = create_new_courier
        with allure.step(f"Авторизуемся созданным курьером с некорректными данными в поле {key}"):
            courier[key] = value
            response = CourierMethods.login_courier(courier["login"], courier["password"])
            assert response.status_code == LoginCourierResponses.NOT_FOUND_404["status_code"]
            assert response.json()["message"] == LoginCourierResponses.NOT_FOUND_404["message"]
