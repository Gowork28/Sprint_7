import pytest
import allure

from methods.order_methods import OrderMethods

class TestAcceptOrder:

    @allure.title("Код 200 после успешного принятия заказа")
    def test_accept_order_success(self, get_courier_id_and_delete, get_order_id_and_delete):
        courier_id = get_courier_id_and_delete
        order_id = get_order_id_and_delete
        response = OrderMethods.accept_order(order_id, courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True} # Код 409 вместо 200 при попытке отменить заказ после принятия


    @pytest.mark.parametrize("parameter, test_data",
                             [
                                 ("id", ""),
                                 ("courierId", ""),
                             ])
    @allure.title("Код 400 при попытке принять заказ без id заказа или курьера")
    def test_accept_order_without_id_failed(self, get_courier_id_and_delete, get_order_id_and_delete, parameter, test_data):
        courier_id = get_courier_id_and_delete
        order_id = get_order_id_and_delete
        data_dict = {"id": order_id,
                     "courierId": courier_id}
        data_dict[parameter] = test_data
        response = OrderMethods.accept_order(data_dict["id"], data_dict["courierId"])
        assert response.status_code == 400 # ошибка 404 вместо 400 при попытке отправить запрос без id заказа
        assert response.json()["message"] == "Недостаточно данных для поиска"


    @pytest.mark.parametrize("parameter, test_data, expected_result",
                             [
                                 ("id", "55", "Заказа с таким id не существует"),
                                 ("courierId", "55", "Курьера с таким id не существует"),
                             ])
    @allure.title("Код 404 при попытке принять заказ с неверным id заказа или курьера")
    def test_accept_order_non_existing_id_failed(self, get_courier_id_and_delete, get_order_id_and_delete, parameter, test_data, expected_result):
        courier_id = get_courier_id_and_delete
        order_id = get_order_id_and_delete
        data_dict = {"id": order_id,
                     "courierId": courier_id}
        data_dict[parameter] = test_data
        response = OrderMethods.accept_order(data_dict["id"], data_dict["courierId"])
        assert response.status_code == 404
        assert response.json()["message"] == expected_result