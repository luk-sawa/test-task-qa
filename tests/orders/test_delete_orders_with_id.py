import pytest
import requests
from ..framework.data import url_address


def test_delete_orders_with_id(prepare_order):
    premade_order_id = prepare_order['orderID']
    response = requests.delete(f'{url_address()}/orders/{premade_order_id}')
    assert response.status_code == 204
    assert orders_are_empty()


def test_delete_orders_with_incorrect_id(prepare_order):
    response = requests.delete(f'{url_address()}/orders/123')
    response_json = response.json()
    assert response.status_code == 404
    assert response_json['code'] == 404 and response_json['message'] == 'Order not found'
    assert orders_are_not_empty()


def orders_are_empty():
    is_empty = False
    response = requests.get(f'{url_address()}/orders').json()
    if not response:
        is_empty = True
    return is_empty


def orders_are_not_empty():
    is_not_empty = False
    response = requests.get(f'{url_address()}/orders').json()
    if response:
        is_not_empty = True
    return is_not_empty
