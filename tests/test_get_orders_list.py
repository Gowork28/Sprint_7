import allure

from methods.order_methods import OrderMethods


class TestGetOrdersList:

    @allure.title("Код 200 при успешном получении списка заказов")
    def test_get_orders_list_success(self):
        response = OrderMethods().get_list_of_orders()
        assert response.status_code == 200
        assert "orders" in response.json()
        print(response.json())