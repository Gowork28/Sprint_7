import pytest
import allure
from data.test_data import TestDataForOrder
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK GREY"]),
        ([""])])
    @allure.title("Код 201 при успешном создании заказа")
    def test_create_order_success(self, delete_order, color):
        body = TestDataForOrder.VALID_DATA_FOR_ORDER.copy()
        body["color"] = color
        response = OrderMethods.make_order(body)
        assert response.status_code == 201
        assert "track" in response.json()
        track = response.json()["track"]
        delete_order.append(track)
