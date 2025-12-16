import allure

from methods.order_methods import OrderMethods
from data.test_data import CommonResponses

class TestGetOrdersList:

    @allure.title("Код 200 при успешном получении списка заказов")
    def test_get_orders_list_success(self):
        with allure.step("Получаем список заказов"):
            response = OrderMethods().get_list_of_orders()
            assert response.status_code == CommonResponses.OK_200["status_code"]
            assert "orders" in response.json()