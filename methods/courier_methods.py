import requests
import allure
from data.urls import UrlsForTest

class CourierMethods:

    @staticmethod
    @allure.title("Создание курьера")
    def create_courier_data(body):
        return requests.post(url=UrlsForTest.CREATE_COURIER_URL, json=body)

    @staticmethod
    @allure.title("Логин курьера в системе и получение его id")
    def login_courier(login, password):
        params = {
            'login': login,
            'password': password
        }
        return requests.post(url=UrlsForTest.COURIER_LOGIN_URL, json=params)

    @staticmethod
    @allure.title("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(url=f"{UrlsForTest.DELETE_COURIER_URL}/{courier_id}")
