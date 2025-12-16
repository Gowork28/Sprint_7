import random
import string
import pytest

from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
from data.test_data import TestDataForOrder, TestDataForCourier

@pytest.fixture
def existing_courier():
    body = TestDataForCourier.VALID_DATA_FOR_COURIER.copy()
    CourierMethods.create_courier_data(body)

    yield body

    courier_id = CourierMethods.login_courier(body["login"], body["password"])
    CourierMethods.delete_courier(courier_id)


@pytest.fixture
def random_valid_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    body = {}

    body["login"] = generate_random_string(10)
    body["password"] = generate_random_string(10)
    body["firstName"] = generate_random_string(10)

    yield body

    courier_id = CourierMethods.login_courier(body["login"], body["password"])
    CourierMethods.delete_courier(courier_id)

@pytest.fixture
def create_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    body = {}

    body["login"] = generate_random_string(10)
    body["password"] = generate_random_string(10)
    body["firstName"] = generate_random_string(10)

    CourierMethods.create_courier_data(body)
    yield body

    courier_id = CourierMethods.login_courier(body["login"], body["password"])
    CourierMethods.delete_courier(courier_id)

@pytest.fixture
def get_courier_id_and_delete():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    body = {}

    body["login"] = generate_random_string(10)
    body["password"] = generate_random_string(10)
    body["firstName"] = generate_random_string(10)

    CourierMethods.create_courier_data(body)
    r = CourierMethods.login_courier(body["login"], body["password"])
    courier_id = r.json()["id"]

    yield courier_id
    CourierMethods.delete_courier(courier_id)


@pytest.fixture
def delete_order():
    tracks = []
    yield tracks
    for track in tracks:
         OrderMethods.cancel_order(track)

@pytest.fixture
def create_new_order():
    body = TestDataForOrder.VALID_DATA_FOR_ORDER.copy()
    response = OrderMethods.make_order(body)
    track = response.json()["track"]
    yield track
    OrderMethods.cancel_order(track)

@pytest.fixture
def get_order_id_and_delete():
    body = TestDataForOrder.VALID_DATA_FOR_ORDER.copy()
    response = OrderMethods.make_order(body)
    track = response.json()["track"]
    r = OrderMethods.get_order_by_track_number(track)
    order_id = r.json()["order"]["id"]

    yield order_id
    OrderMethods.cancel_order(track)