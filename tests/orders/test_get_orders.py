import pytest
import requests


def test_get_orders(fill_database_with_orders):
    premade_orders_list = fill_database_with_orders
    response = requests.get('http://127.0.0.1:5000/orders')
    assert response.status_code == 200
    assert check_orders_list_content(response.json(), premade_orders_list)


def check_orders_list_content(response_list, database_content_list):
    result = True
    for order in database_content_list:
        order.pop('orderID', None)
    if response_list == database_content_list:
        result = True
    return result
