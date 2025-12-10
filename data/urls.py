class UrlsForTest:

    BASE_URL = 'http://qa-scooter.praktikum-services.ru'

    COURIER_LOGIN_URL = f'{BASE_URL}/api/v1/courier/login'
    CREATE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
    DELETE_COURIER_URL = f'{BASE_URL}/api/v1/courier'

    CREATE_ORDER_URL = f'{BASE_URL}/api/v1/orders'
    ACCEPT_ORDER_URL = f'{BASE_URL}/api/v1/orders/accept'
    GET_ORDER_BY_TRACK_URL = f'{BASE_URL}/api/v1/orders/track'
    GET_LIST_ORDERS_URL = f'{BASE_URL}/api/v1/orders'
    CANCEL_ORDER_URL = f'{BASE_URL}/api/v1/orders/cancel'
    FINISH_ORDER_URL = f'{BASE_URL}/api/v1/orders/finish'