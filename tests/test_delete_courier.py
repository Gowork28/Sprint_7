import pytest
import allure

from methods.courier_methods import CourierMethods
from data.test_data import CommonResponses, DeleteCourierResponses

class TestDeleteCourier:

    @allure.title("Код 200 при успешном удалении курьера")
    def test_delete_courier_success(self, random_valid_courier):
        with allure.step("Создаем курьера"):
            body = random_valid_courier
            CourierMethods.create_courier_data(body)
        with allure.step("Авторизуемся созданным курьером"):
            response = CourierMethods.login_courier(body["login"], body["password"])
        with allure.step("Получаем id курьера"):
            courier_id = response.json()["id"]
        with allure.step("Удаляем курьера"):
            deleted_courier = CourierMethods.delete_courier(courier_id)
            assert deleted_courier.status_code == CommonResponses.OK_200["status_code"]
            assert deleted_courier.json() == CommonResponses.OK_200["message"]

    @pytest.mark.parametrize('new_id', ['0', '10000000', '-1'])
    @allure.title("Код 404 при удалении курьера с несуществующим id")
    def test_delete_courier_with_non_existing_id_failed(self, new_id):
        with allure.step("Удаляем курьера"):
            response = CourierMethods.delete_courier(new_id)
            assert response.status_code == DeleteCourierResponses.NOT_FOUND_404["status_code"]
            assert response.json()["message"] == DeleteCourierResponses.NOT_FOUND_404["message"]

    @allure.title("Код 400 при удалении курьера без передачи id")
    def test_delete_courier_with_empty_id(self):
        with allure.step("Удаляем курьера"):
            response = CourierMethods.delete_courier(courier_id='')
            assert response.status_code == DeleteCourierResponses.BAD_REQUEST_400["status_code"]
            assert response.json()["message"] == DeleteCourierResponses.BAD_REQUEST_400["message"]


