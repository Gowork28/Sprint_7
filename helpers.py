from data.test_data import TestDataForOrder

def modify_valid_data_for_order(key, value):
    body = TestDataForOrder.VALID_DATA_FOR_ORDER.copy()
    body[key] = value
    return body