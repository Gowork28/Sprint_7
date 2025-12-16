import pytest
import allure
from data.test_data import TestDataForOrder, CommonResponses
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK, GREY"]),
        ([""])])
    @allure.title("Код 201 при успешном создании заказа")
    def test_create_order_success(self, delete_order, color):
        with allure.step("Формируем тело запроса с тестовыми данными"):
            body = TestDataForOrder.VALID_DATA_FOR_ORDER.copy()
            body["color"] = color
        with allure.step("Создаем заказ"):
            response = OrderMethods.make_order(body)
            assert response.status_code == CommonResponses.CREATED_201["status_code"]
            assert "track" in response.json()
            track = response.json()["track"]
        with allure.step("Удаляем заказ"):
            delete_order.append(track)
