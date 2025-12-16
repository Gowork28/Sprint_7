import pytest
import allure

from methods.order_methods import OrderMethods
from data.test_data import CommonResponses, GetOrderTrackResponses

class TestGetOrderByTrack:

    @allure.title("Код 200 при успешном получении заказа по его номеру")
    def test_get_order_by_track_success(self, create_new_order):
        with allure.step("Создаем заказ и получаем его номер"):
            track = create_new_order
        with allure.step("Получаем заказ"):
            response = OrderMethods.get_order_by_track_number(track)
            assert response.status_code == CommonResponses.OK_200["status_code"]
            assert "order" in response.json()

    @allure.title("Код 400 попытке получить заказ без номера")
    def test_get_order_without_track_failed(self):
        with allure.step("Получаем заказ"):
            track = None
            response = OrderMethods.get_order_by_track_number(track)
            assert response.status_code == GetOrderTrackResponses.BAD_REQUEST_400["status_code"]
            assert response.json()["message"] == GetOrderTrackResponses.BAD_REQUEST_400["message"]

    @pytest.mark.parametrize("track_number", ["0", "999999999"])
    @allure.title("Код 404 при попытке получить заказ по несуществующему номеру")
    def test_get_order_non_existing_track_failed(self, track_number):
        with allure.step("Получаем заказ"):
            track = track_number
            response = OrderMethods.get_order_by_track_number(track)
            assert response.status_code == GetOrderTrackResponses.NOT_FOUND_404["status_code"]
            assert response.json()["message"] == GetOrderTrackResponses.NOT_FOUND_404["message"]