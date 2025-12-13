import pytest
import allure

from methods.order_methods import OrderMethods


class TestGetOrderByTrack:

    @allure.title("Код 200 при успешном получении заказа по его номеру")
    def test_get_order_by_track_success(self, create_new_order):
        track = create_new_order
        response = OrderMethods.get_order_by_track_number(track)
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Код 400 попытке получить заказ без номера")
    def test_get_order_without_track_failed(self):
        track = None
        response = OrderMethods.get_order_by_track_number(track)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @pytest.mark.parametrize("track_number", ["0", "999999999"])
    @allure.title("Код 400 при попытке получить заказ по несуществующему номеру")
    def test_get_order_non_existing_track_failed(self, track_number):
        track = track_number
        response = OrderMethods.get_order_by_track_number(track)
        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"