import requests
import allure
from data.urls import UrlsForTest

class OrderMethods:

    @staticmethod
    @allure.title("Создание заказа")
    def make_order(body):
        return requests.post(url=UrlsForTest.CREATE_ORDER_URL, json=body)

    @staticmethod
    @allure.title("Принять заказ")
    def accept_order(order_id, courier_id):
        return requests.put(url=f"{UrlsForTest.ACCEPT_ORDER_URL}/{order_id}", params = {"courierId": courier_id})

    @staticmethod
    @allure.title("Получить заказ по его номеру")
    def get_order_by_track_number(track):
        return requests.get(url=UrlsForTest.GET_ORDER_BY_TRACK_URL, params={"t": track})

    @staticmethod
    @allure.title("Получение списка заказов")
    def get_list_of_orders():
        return requests.get(url=UrlsForTest.GET_LIST_ORDERS_URL)

    @staticmethod
    @allure.title("Отменить заказ")
    def cancel_order(track):
        return requests.put(url=UrlsForTest.CANCEL_ORDER_URL, params = {"track": track})