import pytest
import allure

from methods.order_methods import OrderMethods
from data.test_data import CommonResponses, AcceptOrderResponses

class TestAcceptOrder:

    @allure.title("Код 200 после успешного принятия заказа")
    def test_accept_order_success(self, get_courier_id_and_delete, get_order_id_and_delete):
        with allure.step("Создаем курьера и получаем его id"):
            courier_id = get_courier_id_and_delete
        with allure.step("Создаем заказ и получаем его id"):
            order_id = get_order_id_and_delete
        with allure.step("Принимаем заказ"):
            response = OrderMethods.accept_order(order_id, courier_id)
            assert response.status_code == CommonResponses.OK_200["status_code"]
            assert response.json() == CommonResponses.OK_200["message"]


    @pytest.mark.parametrize("parameter, test_data",
                             [
                                 ("id", ""),
                                 ("courierId", ""),
                             ])
    @allure.title("Код 400 при попытке принять заказ без id заказа или курьера")
    def test_accept_order_without_id_failed(self, get_courier_id_and_delete, get_order_id_and_delete, parameter, test_data):
        with allure.step("Создаем курьера и получаем его id"):
            courier_id = get_courier_id_and_delete
        with allure.step("Создаем заказ и получаем его id"):
            order_id = get_order_id_and_delete
        with allure.step(f"Подменяем тестовые данные {parameter}"):
            data_dict = {"id": order_id,
                         "courierId": courier_id}
            data_dict[parameter] = test_data
        with allure.step("Принимаем заказ"):
            response = OrderMethods.accept_order(data_dict["id"], data_dict["courierId"])
            assert response.status_code == AcceptOrderResponses.CONFLICT_400["status_code"]
            assert response.json()["message"] == AcceptOrderResponses.CONFLICT_400["message"]


    @pytest.mark.parametrize("parameter, test_data, expected_result",
                             [
                                 ("id", "55", "Заказа с таким id не существует"),
                                 ("courierId", "55", "Курьера с таким id не существует"),
                             ])
    @allure.title("Код 404 при попытке принять заказ с неверным id заказа или курьера")
    def test_accept_order_non_existing_id_failed(self, get_courier_id_and_delete, get_order_id_and_delete, parameter, test_data, expected_result):
        with allure.step("Создаем курьера и получаем его id"):
            courier_id = get_courier_id_and_delete
        with allure.step("Создаем заказ и получаем его id"):
            order_id = get_order_id_and_delete
        with allure.step(f"Подменяем тестовые данные {parameter}"):
            data_dict = {"id": order_id,
                         "courierId": courier_id}
            data_dict[parameter] = test_data
        with allure.step("Принимаем заказ"):
            response = OrderMethods.accept_order(data_dict["id"], data_dict["courierId"])
            assert response.status_code == AcceptOrderResponses.NOT_FOUND_404["status_code"]
            assert response.json()["message"] == expected_result