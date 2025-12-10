import random
import string

class UniqCourierData:

    @staticmethod
    def register_new_courier_and_return_login_password(length=10):
        payload = {
                "login": ''.join(random.choice(string.ascii_lowercase,k=length)),
                "password": ''.join(random.choice(string.ascii_lowercase,k=length)),
                "firstName": ''.join(random.choice(string.ascii_lowercase,k=length))
        }
        print(payload)


class TestDataForOrder:
    VALID_DATA_FOR_ORDER = {
        "firstName": "Hanna",
        "lastName": "Montana",
        "address": "ChinaTown 67",
        "metroStation": 1,
        "phone": "+7 777 777 77 77",
        "rentTime": 1,
        "deliveryDate": "2025-12-15",
        "comment": "nihao",
        "color": [
            "BLACK"
        ]
    }

