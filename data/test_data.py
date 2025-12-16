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
        "color": ["BLACK"]
    }

class TestDataForCourier:
    VALID_DATA_FOR_COURIER = {
        "login": "starstar3000",
        "password": "12341234",
        "firstName": "twinkle",
    }

class CommonResponses:

     OK_200 = {
         "status_code": 200,
         "message": {"ok": True}
     }

     CREATED_201 = {
         "status_code": 201,
         "message": {"ok": True}
     }

class CreateCourierResponses:

    BAD_REQUEST_400 = {
        "status_code": 400,
        "message": "Недостаточно данных для создания учетной записи"
    }

    CONFLICT_409 = {
        "status_code": 409,
        "message": "Этот логин уже используется"
    }

class LoginCourierResponses:

    BAD_REQUEST_400 = {
        "status_code": 400,
        "message": "Недостаточно данных для входа"
    }

    NOT_FOUND_404 = {
        "status_code": 404,
        "message": "Учетная запись не найдена"
    }

class DeleteCourierResponses:

    BAD_REQUEST_400 = {
        "status_code": 400,
        "message": "Недостаточно данных для удаления курьера"
    }

    NOT_FOUND_404 = {
        "status_code": 404,
        "message": "Курьера с таким id нет"
    }

class AcceptOrderResponses:

    CONFLICT_400 = {
        "status_code": 400,
        "message": "Недостаточно данных для поиска"
    }

    NOT_FOUND_404 = {
        "status_code": 404
    }

class GetOrderTrackResponses:

     BAD_REQUEST_400 = {
        "status_code": 400,
        "message": "Недостаточно данных для поиска"
     }

     NOT_FOUND_404 = {
        "status_code": 404,
        "message": "Заказ не найден"
     }