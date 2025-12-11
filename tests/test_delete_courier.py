import pytest
import allure

from methods.courier_methods import CourierMethods

class TestDeleteCourier:

    @allure.title("Код 200 при успешном удалении курьера")
    def test_delete_courier_success(self, random_valid_courier):
        body = random_valid_courier
        CourierMethods.create_courier_data(body)
        response = CourierMethods.login_courier(body["login"], body["password"])
        courier_id = response.json()["id"]
        deleted_courier = CourierMethods.delete_courier(courier_id)
        assert deleted_courier.status_code == 200
        assert deleted_courier.json() == {"ok": True}

    @pytest.mark.parametrize('new_id', ['0', '10000000', '-1'])
    @allure.title("Код 404 при удалении курьерас несуществующим id")
    def test_delete_courier_with_non_existing_id_failed(self, new_id):
        response = CourierMethods.delete_courier(new_id)
        assert response.status_code == 404

    @allure.title("Код 400 при удалении курьера без передачи id")
    @pytest.mark.xfail(reason="Код 404 вместо 400 при отправке запроса без id")
    def test_delete_courier_with_empty_id(self):
        response = CourierMethods.delete_courier(courier_id='')
        assert response.status_code == 400





